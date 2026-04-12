# DS 4320 Project 2: NBA Aging Curve Database

### Executive Summary

This repository contains the 

### Project Metadata

| Information | Value  |
|:---|:---|
| Name | Brian Hockett |
| NetID | mgh2xx |
| DOI | [https://doi.org/10.5281/zenodo.19544215](https://doi.org/10.5281/zenodo.19544215)
| Press Release | [Individualized Aging Curves Reveal That No Two NBA Players Evolve the Same Way](https://github.com/brianhockett/nba-aging-curve/blob/main/PressRelease.md) |
| Pipeline | [Analysis Pipeline (.ipynb)](https://github.com/brianhockett/nba-aging-curve/blob/main/pipeline.ipynb) + [Analysis Pipeline (.md)](https://github.com/brianhockett/nba-aging-curve/blob/main/pipeline.md) |
| License | [MIT](https://github.com/brianhockett/nba-aging-curve/blob/main/LICENSE) |

## Problem Definition

### General and Specific Problem

- **General Problem:** Projecting athletic performance. Projecting NBA player performance.

- **Specific Problem:** Predicting how NBA player Box Plus Minus (BPM) changes as a function of age, position, and injury history in order to model career aging curves that inform future player progression or regression.

### Motivation
Athletic performance changing with age is a universal phenomenon across all major sports, and the NBA is no exception. Players are typically understood to come into the NBA young and inexperienced, improve year-over-year until they enter their "prime", then begin to slowly regress until retirement. However, this trajectory is not the same for every player. In recent years, we have seen players like LeBron James and Steph Curry continue their elite performance into their late 30s, while other players seem to fall off significantly earlier. This project aims to address the non-universal nature of NBA player aging, by predicting an aging curve for each player in isolation, rather than assuming the same trend for every player. The result is a more accurate picture of how any given player's performance is likely to evolve, which is useful for front offices weighing contract decisions, analysts studying positional aging patterns, or anyone trying to understand where a player stands in their career arc.

### Rationale
The first step in the refinement was defining the term "performance", a very broad term for athletes. The choice was made to use Box Plus Minus (BPM) as the proxy for performance, as it is a single catch-all metric that estimates the on-court value of a player on a rate basis. Since it is a rate-based statistic, it will be effective for estimating the value of players with lower playing time. The next step was the choice to focus on aging curves specifically, as the trajectory of player decline is a question that manifests differently across sports and individuals. Likewise, recent history in the NBA has brought into question existing beliefs about how players age, which this project would be able to address. Lastly, the choice to include position and injury history as explicitly named variables in the aging curve was made due to their direct relevance to future availability and the rate at which different physical skills deteriorate.


### Press Release Headline and Link
[**Individualized Aging Curves Reveal That No Two NBA Players Evolve the Same Way**](https://github.com/brianhockett/nba-aging-curve/blob/main/PressRelease.md)

## Domain Exposition

### Terminology
**NBA Terminology**

| Term | Abbr | Definition |
|:------|:------|:------------|
| Points Per Game | PPG | Average points scored per game |
| Rebounds Per Game | RPG | Average total rebounds per game |
| Assists Per Game | APG | Average assists per game |
| Blocks Per Game | BPG | Average blocked shots per game |
| Steals Per Game | SPG | Average steals per game |
| Box Plus Minus | BPM | A rate statistic estimating a player's contribution to their team per 100 possessions, relative to a league-average player |
| Offensive Box Plus Minus | OBPM | The offensive component of BPM, measuring a player's offensive contribution per 100 possessions |
| Defensive Box Plus Minus | DBPM | The defensive component of BPM, measuring a player's defensive contribution per 100 possessions |
| Win Shares | WS | An estimate of the number of wins a player contributed to their team over a season |
| Win Shares Per 48 Minutes | WS/48 | Win Shares normalized per 48 minutes, allowing comparison across players with different playing time |
| Value Over Replacement Player | VORP | BPM scaled by minutes played, estimating total value added over a replacement-level player across a full season |
| Replacement Level | — | A performance threshold representing the level of player a team could acquire by signing a freely available player |
| Player Efficiency Rating | PER | A per-minute rating of a player's overall statistical production, normalized to a league average of 15 |
| True Shooting Percentage | TS% | A shooting efficiency metric accounting for field goals, three-pointers, and free throws |
| Aging Curve | — | A model describing how a player's performance metric changes as a function of age across their career |
| Peak Age | — | The age at which a player reaches their highest modeled performance level |
| Games Played | GP | The number of regular season games a player appeared in during a given season |

### Background Information
This project lives at the intersection of the sports analytics and predictive modeling domains, applied to the National Basketball Association. Sports analytics was popularized by its application to baseball in the early 2000s, and has since been applied to most of the major sports, including NBA basketball. The NBA is one of the most statistically rich sports leagues, with verbose play tracking and in-depth metrics capturing player performance and value. This has enabled the rapid growth of sports analytics within the sport of basketball, allowing for further research, exploration, and quantification of player ability. Age curves specifically are one form of predictive modeling that have been applied to sports with much success. They capture general aging trends for the sport as a whole, as well as allow for modeling of future player performance that differs from the league-wide trend. As the NBA continues to evolve, with players remaining competitive later and later into their careers, the ability to model individual aging trajectories with precision has never been more practically relevant.

### Background Reading
| Title | Description | Link |
|:-------|:-------------|:------|
| Player Progression in the NBA | Harvard Sports Analysis study modeling player development using an aging curve and adjusting for survivorship bias | https://myuva-my.sharepoint.com/:b:/g/personal/mgh2xx_virginia_edu/IQBnJYNl2KIdRpH4wXuOz_NPAeeinkm1_qdvLMiO6bMnK7M?e=oUUdzF |
| About Box Plus/Minus (BPM) | Official Basketball Reference documentation explaining the methodology, calculation, and limitations of BPM | https://myuva-my.sharepoint.com/:b:/g/personal/mgh2xx_virginia_edu/IQCXn63OtUsFQa1zjv9FAZucAczVeWmmWj9pxPcBPJ3ZwDU?e=a2Wo7d |
| Is LeBron breaking the aging curve? | ESPN analytics piece analyzing LeBron James' career, examining how his trajectory compares to the expected decline of NBA players | https://myuva-my.sharepoint.com/:b:/g/personal/mgh2xx_virginia_edu/IQC2RLjxa9Q_QqTEOS4Lbjv0ASCKNyvzNMifRudUjrGXCes?e=uc6OAU |
| Inside the Numbers Game: Analytics and the Next Era of Basketball | INFORMS article tracing the full history of NBA analytics from the introduction of play-by-play data to modern player tracking technology | https://myuva-my.sharepoint.com/:b:/g/personal/mgh2xx_virginia_edu/IQD5LiblpC19SbGHcXf4J3jHAds6zy9RV21HlnZnXs-2cGU?e=BPi37H |
| An Approach to Survivor Bias in Baseball | Baseball Prospectus methodology piece demonstrating how survivorship bias distorts aging curves in baseball, and how its effects can be mitigated | https://myuva-my.sharepoint.com/:b:/g/personal/mgh2xx_virginia_edu/IQCuNx5yk0yTR53POq0k2UfxAceCCXC9-0T5WhSUTo1P724?e=7ge330 |

## Data Creation

### Data Acquisition
The raw data was acquired 

### Code Table
| Data | Description | Link to Code |
|:-------------|:-----------|:-------------|
| Basketball Reference Data | Uses `basketball_reference_web_scraper` package to scrape Basketball Reference for player data | [Basketball Reference Code](https://github.com/brianhockett/nba-aging-curve/blob/main/src/generate-br-data.py) |

### Rationale
The 

### Bias Identification
The 

### Bias Mitigation
The 


## Metadata

### Soft-Schema
Guidelines for document structure

### Data Summary
 Summary of Database contents - tabular
form is permissible

### Data Dictionary

**The data dictionary has been separated into two sections. The first contains descriptions and example values for each field. The second contains quantification of uncertainty for numerical features.**

| Field Name | Data Type | Description | Example Value |
|:-------------|:-----------|:-------------|:---------------|
| - | - | - | - | - |


### Data Dictionary Uncertainty
| Field Name | Data Type | Reason for Uncertainty | Quantification of Uncertainty |
|:-------------|:-----------|:-------------------------------|:------|
| - | - | - | - | - |

