import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\preprocessing\batsmenMatchByMatchData.csv')

batsmenOppositionWiseData = df.groupby(['striker', 'bowling_team']).agg(
    Total_Runs=py.NamedAgg(column='Total_Runs', aggfunc='sum'),
    Fours=py.NamedAgg(column='4s', aggfunc='sum'),
    Sixes=py.NamedAgg(column='6s', aggfunc='sum'),
    numberOfDismissals=py.NamedAgg(
        column='Dismissal', aggfunc='sum'),
    Balls_Faced=py.NamedAgg(
        column='Balls_Faced', aggfunc='sum'),
    opposition_wise_Matches_Played=py.NamedAgg(
        column='match_id', aggfunc='count'),
    opposition_wise_dr11=py.NamedAgg(column='dream 11 score', aggfunc='mean')
)
batsmenOppositionWiseData['opposition_wiseStrike_Rate'] = (
    batsmenOppositionWiseData['Total_Runs'] / batsmenOppositionWiseData['Balls_Faced']) * 100
batsmenOppositionWiseData['opposition_wiseAverage'] = batsmenOppositionWiseData.apply(
    lambda row: row['Total_Runs'] / row['opposition_wise_Matches_Played'] if row['numberOfDismissals'] == 0 else row['Total_Runs'] / row['numberOfDismissals'], axis=1
)
batsmenOppositionWiseData.reset_index(inplace=True)
batsmenOppositionWiseData.to_csv('batsmenOppositionWiseData.csv', index=False)
