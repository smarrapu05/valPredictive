# Valorant Predictive Model

This model uses the data from VCT 2024 matches in order to create a logistic regression model that predicts the probability of certain team winning any given match based on certain historical stats (such as Average Combat Score per Player). \

## vlrWebScraper
This folder contains the python web scraper used to take statistics from vlr.gg. If you put an event (such as Americas kickoff 2024) into find.txt and run linkfinder.py, it will put all the match links from that event into links.txt. Running main.py will take all the links from links.txt and put the statistics into data.csv. It contains the following columns: \ 
**ACS**: The aggregate ACS of each player on a team during a match\
**KpR**: The total kills of a team during a match\
**DpR**: The total deaths of a team during a match\
**ApR**: The total assists of a team during a match\
**KAST**: The total KAST of a team during a match\
**ADR**: The aggregate ADR of each player on a team during a match\
**HS**: The total headshot percentage of the team during a match\
**FK**: The total first kills of a team during a match\
**FD**: The total first deaths of a team during a match\
**W.L**: Whether the team won or lost the match\

## Final model

All of the data manipulation and the resulting model is contained in vct24datamanip.Rmd. In order to see the writeup install and open vct24datamanip.html. A pdf version is also available, however the formatting has some issues.