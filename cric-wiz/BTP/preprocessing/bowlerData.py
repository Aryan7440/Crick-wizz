import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\preprocessing\bowlerMatchByMatchData.csv')
bowlerData = df.groupby(['bowler']).agg(
    Runs_Conceded=py.NamedAgg(column='Runs_Conceded', aggfunc='sum'),
    Wickets_Taken=py.NamedAgg(
        column='Wickets_Taken', aggfunc='sum'),
    balls_bowled=py.NamedAgg(column='balls_bowled', aggfunc='sum'),
    Matches_Played=py.NamedAgg(column='venue', aggfunc='count'),
    five_wickets_haul=py.NamedAgg(column='5ws', aggfunc='sum'),
    three_wickets_haul=py.NamedAgg(column='3ws', aggfunc='sum'),
    four_wickets_haul=py.NamedAgg(column='4ws', aggfunc='sum'),
    maidens=py.NamedAgg(column='maidens', aggfunc='sum'),
    avg_drm11_score=py.NamedAgg(column='dream 11 score', aggfunc='mean'),
)
bowlerData['Economy'] = (
    (bowlerData['Runs_Conceded']*6)/(bowlerData['balls_bowled']))
bowlerData['strike_rate'] = bowlerData.apply(
    lambda row: row['balls_bowled'] / row['Wickets_Taken'] if row['Wickets_Taken'] != 0 else row['balls_bowled']+row['Matches_Played'], axis=1
)

# Reset index
bowlerData.reset_index(inplace=True)
bowlerData.to_csv(
    'bowlerData.csv', index=False)
