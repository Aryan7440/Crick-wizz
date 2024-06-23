import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\preprocessing\batsmenMatchByMatchData.csv')
batsmenData = py.read_csv(r'D:\ML\BTP\preprocessing\batsmenData.csv')
batsmenOppositon = py.read_csv(
    r'D:\ML\BTP\preprocessing\batsmenOppositionWiseData.csv')
batsmenOppositon = batsmenOppositon[[
    'striker', 'bowling_team', 'opposition_wise_Matches_Played', 'opposition_wiseStrike_Rate', 'opposition_wiseAverage', 'opposition_wise_dr11']]
# rankings_pd.rename(columns={'Matches_Played': 'TEST'}, {'Strike_Rate': 'TEST'}, {'Average': 'TEST'}, {'Matches_Played': 'TEST'}, {'Matches_Played': 'TEST'}, inplace=True)
batsmenVenue = py.read_csv(
    r'D:\ML\BTP\preprocessing\batsmenVenueWiseData.csv')
batsmenVenue = batsmenVenue[[
    'striker', 'venue', 'venueWise_Matches_Played', 'venueWise_Strike_Rate', 'venueWise_Average', 'venueWise_dr11']]

batsmenData = batsmenData[['striker', 'Avg_balls_faced',
                           'Matches_Played', 'Strike_Rate', 'Average', 'avg_drm11_score']]
venuedata = py.read_csv(
    r'D:\ML\BTP\preprocessing\VenueData.csv')
venuedata = venuedata[['venue', 'Venue_Matches_Played',
                      'Venue_Avg_Batsmen_Strike_Rate', 'Venue_Avg_Batsmen_Average', 'Venue_Avg_Bowler_Economy', 'Venue_Avg_Bowler_Average', 'Venue_dream11']]


data = df[['match_id', 'striker', 'venue', 'bowling_team', 'dream 11 score']]
newData = data.merge(batsmenData, on='striker', how='left')
newData = newData.merge(batsmenOppositon, on=[
                        'striker', 'bowling_team'], how='left')
newData = newData.merge(batsmenVenue, on=['striker', 'venue'], how='left')
newData = newData.merge(venuedata, on=['venue'], how='left')
newData.drop('match_id', axis=1, inplace=True)
newData.to_csv('final_batsmen.csv', index=False)
