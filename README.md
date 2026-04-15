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

The data used for this project originated on the basketball stats website, `basketball-reference.com`. The data was acquired from the website by reading the html of the basic and advanced stats pages for each season included for the project. These pages contain basic and advanced statistics for every player in a given season. The data generating script scraped the data from both pages for each season, collecting the data from the tables stored on the page. The data for each table was aggregated across all the seasons in the dataset. Finally, the full basic and advanced datasets were combined into a complete dataset. This complete dataset was then aggregated by player into a document style format, where each document contained all seasons of data for a given player. Finally, these documents were loaded into and stored in a MongoDB database collection.

### Code Table
| Data | Description | Link to Code |
|:-------------|:-----------|:-------------|
| Basketball Reference Data | Pulls basic and advanced player statistics data from Basketball Reference and loads it into MongoDB database | [Basketball Reference Code](https://github.com/brianhockett/nba-aging-curve/blob/main/src/generate-br-data.py) |

### Rationale
A number of key decisions had to be made in the data collection process. First, the decision about which years of data had to be made. The choice to collect data from the 2003-04 season to the 2025-26 season was made to ensure a significant sample size, and because it ensures that players' full careers are included in the dataset. This allows for the aging curve model to capture trends over the course of full playing careers (ages 18-40), rather than being cut off half way through most careers. Next, the choice was made to include only regular season data. The exclusion of playoff data was intentional, as many players do not have the opportunity to play in the playoffs, due to circumstances outside of their control. Likewise, the playing environments of the playoffs and regular season are not equivalent, which would lead to skewed results if the playoffs were included. Lastly, in the analysis stage, the dataset will be further restricted to exclude player-seasons in which the player played too few games or too few minutes per game, as their statistical results will not be representative of their true talent, which the model will aim to capture.

### Bias Identification
The most significant source of bias in the dataset for this project is survivorship bias. At the older end of the age spectrum, the majority of the players remaining in the dataset will be those who are playing at a high level. Whereas younger players would be kept on NBA rosters despite poor performance due to their potential for growth, veterans are not given this same opportunity to improve, and are far more likely to be cut (removed from the dataset) if their performance begins to slip. This creates a survivorship bias in the dataset, where the older age groups have artificially better performance, due to the removal of poorly performing players. Likewise, the use of the minutes-per-game and games-played filters creates another form of selection bias, with oft-injured and and low playing time players being excluded from the analysis. This could result in an under-representation of these two groups of players in the aging-curve model. Another form of bias that could be introduced is temporal bias, stemming from the use of data stretching from 2003 to 2026. During this time, the style of play in the NBA changed drastically with the growth of 3-point rates and offensively-focused rule changes resulting in a much higher scoring environment. This leads to a temporal bias where the offensive outputs of players who played in the earlier years of the dataset are systematically lower than those of later-year players.

### Bias Mitigation
Several steps were taken during the data collection and analysis processes to mitigate biases. One of these steps was making use of a mixed effects model for the aging curve in order to address the survivorship bias in older players. By nature of mixed effects models, which will model each player's aging curve individually, rather than as a collection of all the players, the effects of the survivorship bias will be partially mitigated. Players' aging trajectories will be estimated largely based on their own playing history, rather than being distorted by the high-performing veterans in the data. Likewise, the temporal bias caused by using data ranging from 2003 to 2026 will be mitigated through the use of the Box Plus/Minus (BPM) metric to evaluate player performance. While offensive output is systematically biased based on the season the data is from, BPM is normalized on a per-season basis, meaning two players from different seasons will have comparable BPMs, as long as their statistical outputs are similar relative to their season. This normalization mitigates the effects of this bias in the analysis. Finally, while the minutes-per-game and games-played filters introduced a form of selection bias by excluding low-usage and frequently injured players, this restriction was necessary to reduce noise in the performance metrics, as extremely small sample sizes can produce highly volatile BPM estimates that would distort the aging-curve model if they remained in the dataset.


## Metadata

### Soft-Schema

- **There is a single collection in the MongoDB Database, called `players`**
- **Every document in the database represents a single player**
- **Player-Level fields include:**
  - **`_id`: Unique identifier derived from the player's name (e.g. `lastName_firstName`)**
  - **`name`: Full name of the player**
  - **`seasons`: Array of season-level records for the player's career**
- **Season-Level fields include:**
  - **`season`: Season identifier (e.g. `YYYY-YY)**
  - **`age`: Age of the player during that season**
  - **Additional performance metrics (as defined in the data dictionary)**
- **Each player document only contains seasons in which the player appeared. It does not include missing or unused seasons across the full timeline of the dataset (2003–2026)**


**Structure of documents in .json format:**
```{json}
[
    {
        _id: <unique_player_identifier>,
        name: <player_name>,
        seasons: [
            {
                season: <season_identifier>,
                age: <age_value>,
                team: <team_value>,
                ...,
                BPM: <BPM_value>,
                VORP: <VORP_value>
            },
            {
                season: <season_identifier>,
                age: <age_value>,
                team: <team_value>,
                ...,
                BPM: <BPM_value>,
                VORP: <VORP_value>
            },
            ...
        ]
    },
    {
        _id: <unique_player_identifier>,
        name: <player_name>,
        seasons: ...
    },
    ...
]
```

### Data Summary

| Level | Name/Identifier | Description | Quantity |
|:------|:-----|:------------|:---------|
| Database | `bref-data` | MongoDB Database containing `players` collection | 1 |
| Collection | `players` | Collection holding all player documents | 1 |
| Document | Player (`_id`) | Each document represents a player, containing all statistical data for their career. Uniquely identified by `_id` | 2380 |


### Data Dictionary

**The data dictionary has been separated into two sections. The first contains descriptions and example values for each field. The second contains quantification of uncertainty for numerical features.**

| Field Name | Data Type | Description | Example Value |
|:-------------|:-----------|:-------------|:---------------|
| _id | String | Unique identifier for each document in MongoDB | "tracy_mcgrady" |
| name | String | Full name of the player the document represents | "Tracy McGrady" |
| seasons | Array | Array containing season-level performance records for the player | [ {...}, {...} ] |
| seasons.season | String | NBA season identifier in "YYYY-YY" format| "2003-04" |
| seasons.age | Integer | Age of the player during the season | 24 |
| seasons.team | String | Abbreviation of the player's team name for the season | "ORL" |
| seasons.games_played | Integer | The number of games the player appeared in | 67 |
| seasons.games_started | Integer | The number of games the player started | 67 |
| seasons.games_missed | Integer | The number of games the player missed | 15 |
| seasons.injury_flag | Boolean | Indicator of whether the player missed more than half of their possible games | false |
| seasons.minutes_per_game | Float | Average minutes played per game | 39.9 |
| seasons.points_per_game | Float | Average points scored per game | 28 |
| seasons.rebounds_per_game | Float | Average rebounds per game | 6 |
| seasons.assists_per_game | Float | Average assists per game | 5.5 |
| seasons.steals_per_game | Float | Average steals per game | 1.4 |
| seasons.blocks_per_game | Float | Average blocks per game | 0.6 |
| seasons.turnovers_per_game | Float | Average turnovers per game | 2.7 |
| seasons.PER | Float | Player Efficiency Rating (Measure of overall statistical production) for the season | 25.3 |
| seasons.TS_pct | Float | True Shooting Percentage, measuring scoring efficiency | 0.526 |
| seasons.USG_pct | Float | Usage Rate, estimating the share of the team's plays that are used by the player | 33.2 |
| seasons.AST_pct | Float | Assist Rate, estimating the percentage of teammate field goals assisted by the player | 28.3 |
| seasons.TOV_pct | Float | Turnover Rate, estimating the percentage of plays the player turns the ball over | 9.1 |
| seasons.WS | Float | Win Shares, estimating the number of team win added by the player | 8.4 |
| seasons.BPM | Float | Box Plus/Minus, estimating the player's value per 100 possessions relative to league average | 6.4 |
| seasons.VORP | Float | Value Over Replacement Player, estimating value relative to a freely available player | 5.7 |

### Data Dictionary Uncertainty
| Field Name | Data Type | Reason for Uncertainty | Quantification of Uncertainty |
|:-------------|:-----------|:-------------------------------|:------|
| seasons.games_missed | Integer | Games missed is calculated as games played subtracted from a baseline of the max number of games any team played in that season. There are some players in the dataset who were traded mid-season, and would have more or less games they could have appeared in than the baseline. | ± 2 games |
| seasons.injury_flag | Boolean | The injury flag is calculated as whether or not a player missed more than half of their possible games. Because this value is derived from seasons.games_missed, it inherits some of its uncertainty. | ~5% of flags incorrect |
| seasons.PER | Float | PER compresses overall box score production into a single value, but is sensitive to era adjustments and cannot fully separate player quality from pace and role context.  | ± 1.5 PER points |
| seasons.WS | Float | Win Shares attributes team wins to individuals using box score proxies, which can over-credit players on strong teams and under-credit those on weaker teams. | ± 1.0 win shares |
| seasons.BPM | Float | BPM estimates impact from box score and lineup proxies, but struggles with non-box-score contributions and role-dependent players. | ± 0.5–1.0 BPM |
| seasons.VORP | Float | VORP compounds BPM and minutes played, so any error in estimated impact or playing time directly propagates into total value estimates. | ± 0.3–0.6 VORP |


