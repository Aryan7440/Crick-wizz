import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\preprocessing\batsmenMatchByMatchData.csv')

batsmenVenueWiseData = df.groupby(['striker', 'venue']).agg(
    Total_Runs=py.NamedAgg(column='Total_Runs', aggfunc='sum'),
    Fours=py.NamedAgg(column='4s', aggfunc='sum'),
    Sixes=py.NamedAgg(column='6s', aggfunc='sum'),
    numberOfDismissals=py.NamedAgg(
        column='Dismissal', aggfunc='sum'),
    Balls_Faced=py.NamedAgg(
        column='Balls_Faced', aggfunc='sum'),
    venueWise_Matches_Played=py.NamedAgg(column='match_id', aggfunc='count'),
    venueWise_dr11=py.NamedAgg(column='dream 11 score', aggfunc='mean')
)
batsmenVenueWiseData['venueWise_Strike_Rate'] = (
    batsmenVenueWiseData['Total_Runs'] / batsmenVenueWiseData['Balls_Faced']) * 100
batsmenVenueWiseData['venueWise_Average'] = batsmenVenueWiseData.apply(
    lambda row: row['Total_Runs'] / row['venueWise_Matches_Played'] if row['numberOfDismissals'] == 0 else row['Total_Runs'] / row['numberOfDismissals'], axis=1
)
batsmenVenueWiseData.reset_index(inplace=True)
batsmenVenueWiseData.to_csv('batsmenVenueWiseData.csv', index=False)
