import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\preprocessing\MatchData.csv')
VenueData = df.groupby(['venue']).agg(
    Total_Runs=py.NamedAgg(column='Total_Runs', aggfunc='sum'),
    Total_Extras=py.NamedAgg(column='Total_Extras', aggfunc='sum'),
    Total_Wickets=py.NamedAgg(
        column='Wickets_Taken', aggfunc='sum'),
    Venue_Matches_Played=py.NamedAgg(column='match_id', aggfunc='count'),
    fours=py.NamedAgg(column='fours', aggfunc='sum'),
    sixes=py.NamedAgg(column='sixes', aggfunc='sum'),
    Total_Balls=py.NamedAgg(column='balls_bowled', aggfunc='sum'),
    Venue_dream11=py.NamedAgg(column='d11', aggfunc='mean')
)

VenueData['Venue_Avg_Batsmen_Strike_Rate'] = (
    VenueData['Total_Runs'] / VenueData['Total_Balls']) * 100
VenueData['Venue_Avg_Batsmen_Average'] = VenueData.apply(
    lambda row: row['Total_Runs'] / row['Matches_Played'] if row['Total_Wickets'] == 0 else row['Total_Runs'] / row['Total_Wickets'], axis=1
)
VenueData['Venue_Avg_Bowler_Economy'] = (
    (VenueData['Total_Runs']*6)/(VenueData['Total_Balls']))
VenueData['Avg_Bowler_strike_rate'] = VenueData.apply(
    lambda row: row['Total_Balls'] / row['Total_Wickets'] if row['Total_Wickets'] != 0 else row['Total_Balls']+row['Matches_Played'], axis=1
)
VenueData['Venue_Avg_Bowler_Average'] = VenueData.apply(
    lambda row: row['Total_Runs'] / row['Total_Wickets'] if row['Total_Wickets'] != 0 else row['Total_Runs'], axis=1
)
VenueData.reset_index(inplace=True)
VenueData.to_csv('VenueData.csv', index=False)
