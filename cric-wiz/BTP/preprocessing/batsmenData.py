import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\preprocessing\batsmenMatchByMatchData.csv')

batsmenData = df.groupby(['striker']).agg(
    Total_Runs=py.NamedAgg(column='Total_Runs', aggfunc='sum'),
    total_dismissals=py.NamedAgg(
        column='Dismissal', aggfunc='sum'),
    balls_faced=py.NamedAgg(column='Balls_Faced', aggfunc='sum'),
    Avg_balls_faced=py.NamedAgg(column='Balls_Faced', aggfunc='mean'),
    Matches_Played=py.NamedAgg(column='match_id', aggfunc='count'),
    Strike_Rate=py.NamedAgg(column='Strike_Rate', aggfunc='mean'),
    avg_drm11_score=py.NamedAgg(column='dream 11 score', aggfunc='mean'),
)
batsmenData.reset_index(inplace=True)
batsmenData['Average'] = batsmenData.apply(
    lambda row: row['Total_Runs'] / row['Matches_Played'] if row['total_dismissals'] == 0 else row['Total_Runs'] / row['total_dismissals'], axis=1
)


batsmenData.to_csv(
    'batsmenData.csv', index=False)
