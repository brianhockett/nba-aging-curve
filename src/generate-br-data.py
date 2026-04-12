# Imports
from collections import defaultdict
from dotenv import load_dotenv
import pandas as pd
import logging
import random
import pymongo
import json
import time
import os
import re

# Initialize logging
logging.basicConfig(
    filename = "generate-br-data.log",                    # Log output file
    level = logging.INFO,
    format= " %(asctime)s - %(levelname)s - %(message)s"  # Timestamp, level, and message format
)

# Load environment variables from .env file
load_dotenv()

# Load MongoDB credentials from .env
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
MONGO_APP_NAME = os.getenv("MONGO_APP_NAME")

# Connection string and client connection
conn = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/?appName={MONGO_APP_NAME}"
client = pymongo.MongoClient(conn)
logging.info("Connected to MongoDB")
print("Connected to MongoDB")

# Select database and collection
db = client['bref-data']
collection = db['players']

# Clear collection before inserting new data
collection.drop()
logging.info("Cleared existing data from MongoDB collection")
print("Cleared existing data from MongoDB collection")

# Configuration
seasons = ["2003-04", "2004-05", "2005-06", "2006-07",
           "2007-08", "2008-09", "2009-10", "2010-11",
           "2011-12", "2012-13", "2013-14", "2014-15",
           "2015-16", "2016-17", "2017-18", "2018-19",
           "2019-20", "2020-21", "2021-22", "2022-23",
           "2023-24", "2024-25", "2025-26"]
delay = 3.5 # 3.5s delay is required for BRef rate limits
output_all = "bref-data.json"      
output_one = "bref-sample-document.json"
save_local = True # Set to True to save the full dataset to a local JSON file


# Function to safely convert values to float
def safe_float(val):
    try:
        if pd.isna(val):
            return None
        return float(val)
    except (ValueError, TypeError):
        return None

# Function to safely convert values to int
def safe_int(val):
    try:
        if pd.isna(val):
            return None
        return int(val)
    except (ValueError, TypeError):
        return None

# Convert season string to BRef year format
def format_bref_year(season_str):
    return str(int(season_str[:4]) + 1)

# Function to create clean ids for MongoDB documents
def clean_id(name):
    name = name.lower().replace(" ", "_")
    name = re.sub(r'[^a-z0-9_]', '', name)
    return name

# Function to fetch one season of stats for all players from BRef
def fetch_season(season_str, measure_type):
    # Convert the inputted season string into BRef's year format
    year = format_bref_year(season_str)
    
    # Use per-game url for base stats, and advanced url for advanced stats
    if measure_type == "Base":
        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    else:
        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_advanced.html"

    # Log and print the fetch attempt
    logging.info(f"Fetching {measure_type} stats for {season_str} (BRef Year: {year})")
    print(f"Fetching {measure_type} stats for {season_str} (BRef Year: {year})")

    # Fetch the tables from the URL using pandas
    try:
        # Use pandas to read the HTML tables from the page
        tables = pd.read_html(url)
        time.sleep(delay)
        
        # Get the first table on the page, which contains the player stats
        df = tables[0]
        
        # Clean mid-table headers that are repeated for readability on BRef pages
        df = df[df['Player'] != 'Player']

        # Remove league average row
        df = df[df['Player'] != 'League Average']
        
        # Remove asterisks from Hall of Fame player names
        if 'Player' in df.columns:
            df['Player'] = df['Player'].str.replace('*', '', regex = False)
            
        # Handle players traded mid-season (BRef shows a "TOT" total row, plus a row for each team)
        # Drop duplicates by player to just keep their "TOT" (Total) stat line for the year.
        df = df.drop_duplicates(subset = ['Player'], keep = 'first')
        
        # Add the season string to the DataFrame for later merging
        df["Season"] = season_str
        return df.to_dict(orient = "records")

    except Exception as e:
        logging.error(f"Failed {measure_type} {season_str}: {e}")
        return []

# Function to merge one base and one advanced row into a single season subdocument
def build_season_dict(base_row, adv_row):
    # Calculate games played
    gp = safe_int(base_row.get("G")) or 1

    # Build the season dictionary, combining base and advanced stats, and calculating derived fields
    return {
        # Basic info
        "season":           base_row.get("Season"),
        "age":              safe_int(base_row.get("Age")),
        "team":             base_row.get("Team"),
        "games_played":     safe_int(base_row.get("G")),
        "games_started":    safe_int(base_row.get("GS")),
        "games_missed":     82 - gp,
        "injury_flag":      gp < 40,
        "minutes_per_game": safe_float(base_row.get("MP")),

        # Counting stats (Per Game mode)
        "points_per_game":    safe_float(base_row.get("PTS")),
        "rebounds_per_game":  safe_float(base_row.get("TRB")),
        "assists_per_game":   safe_float(base_row.get("AST")),
        "steals_per_game":    safe_float(base_row.get("STL")),
        "blocks_per_game":    safe_float(base_row.get("BLK")),
        "turnovers_per_game": safe_float(base_row.get("TOV")),

        # Advanced metrics 
        "PER":      safe_float(adv_row.get("PER"))   if adv_row else None,
        "TS_pct":   safe_float(adv_row.get("TS%"))   if adv_row else None,
        "USG_pct":  safe_float(adv_row.get("USG%"))  if adv_row else None,
        "AST_pct":  safe_float(adv_row.get("AST%"))  if adv_row else None,
        "TOV_pct":  safe_float(adv_row.get("TOV%"))  if adv_row else None,
        "OREB_pct": safe_float(adv_row.get("ORB%"))  if adv_row else None,
        "DREB_pct": safe_float(adv_row.get("DRB%"))  if adv_row else None,
        "WS":       safe_float(adv_row.get("WS"))    if adv_row else None,
        "BPM":      safe_float(adv_row.get("BPM"))   if adv_row else None,
        "VORP":     safe_float(adv_row.get("VORP"))  if adv_row else None,
    }

# Lists to store all data
all_base     = [] 
all_advanced = [] 

# Loop through each season and fetch both base and ad
for season in seasons:
    all_base.extend(fetch_season(season, "Base"))
    all_advanced.extend(fetch_season(season, "Advanced"))

logging.info(f"Collected {len(all_base)} base rows, {len(all_advanced)} advanced rows")
print(f"Collected {len(all_base)} base rows and {len(all_advanced)} advanced rows")

# Index advanced rows by (Player Name, Season) 
advanced_index = {
    (row["Player"], row["Season"]): row
    for row in all_advanced
}

# Group base rows by Player Name
players_base = defaultdict(list)
for row in all_base:
    players_base[row["Player"]].append(row)

# Build one document per player
documents = []

# Loop through each player and their seasons
for player_name, seasons in players_base.items():

    # Sort seasons chronologically for this player
    seasons_sorted = sorted(seasons, key = lambda x: x["Season"])

    # For each season, find the corresponding advanced row and build the season document
    season_docs = []
    for base_row in seasons_sorted:
        key = (player_name, base_row["Season"])
        adv_row = advanced_index.get(key)  
        season_docs.append(build_season_dict(base_row, adv_row))

    # Build the player document by combining their name and all their season sub-documents
    doc = {
        "_id": clean_id(player_name), # Generate a simple string ID
        "name": player_name, 
        "seasons": season_docs
    }
    documents.append(doc)


logging.info(f"Pass 2 complete: {len(documents)} player documents built")
print(f"Built {len(documents)} player documents")

# Insert all player documents into MongoDB collection
if documents:
    collection.insert_many(documents)
    logging.info(f"Inserted {len(documents)} player documents into MongoDB")
    print(f"Inserted {len(documents)} player documents into MongoDB")
else:
    logging.warning("No documents to insert")

# Optionally save the full dataset and a sample document to local JSON files for inspection
if save_local:
    # Save the full dataset to a JSON file
    with open(output_all, "w") as f:
        json.dump(documents, f, indent = 2, default = str)
    print(f"Saved full dataset to {output_all}")

    # Select random sample document
    sample = random.choice(documents)

    # Save sample to separate JSON file
    with open(output_one, "w") as f:
        json.dump(sample, f, indent = 2, default = str)
    print(f"Saved sample document to {output_one}")