import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\preprocessing\all_matches.csv')

# Create a new DataFrame for batsmenMatchByMatchData
batsmenMatchByMatchData = df.groupby(['match_id', 'striker', 'venue', 'bowling_team']).agg(
    Total_Runs=py.NamedAgg(column='runs_off_bat', aggfunc='sum'),
    Total_Extras=py.NamedAgg(column='extras', aggfunc='sum'),
    Bowler=py.NamedAgg(
        column='player_dismissed', aggfunc=lambda x: x.dropna().max()),
    Dismissal_Type=py.NamedAgg(
        column='wicket_type', aggfunc=lambda x: x.dropna().max())
)


batsmenMatchByMatchData['100'] = batsmenMatchByMatchData['Total_Runs'].apply(
    lambda x: 1 if x >= 100 else 0
)
batsmenMatchByMatchData['50'] = batsmenMatchByMatchData['Total_Runs'].apply(
    lambda x: 1 if x >= 50 else 0
)
batsmenMatchByMatchData['30'] = batsmenMatchByMatchData['Total_Runs'].apply(
    lambda x: 1 if x >= 30 else 0
)
batsmenMatchByMatchData['Dismissal'] = batsmenMatchByMatchData['Bowler'].apply(
    lambda x: 1 if py.notna(x) else np.nan)
batsmenMatchByMatchData['Balls_Faced'] = df.groupby(
    ['match_id', 'striker', 'venue', 'bowling_team']).size()
batsmenMatchByMatchData['4s'] = df[df['runs_off_bat'] == 4].groupby(
    ['match_id', 'striker', 'venue', 'bowling_team']).size()
batsmenMatchByMatchData['6s'] = df[df['runs_off_bat'] == 6].groupby(
    ['match_id', 'striker', 'venue', 'bowling_team']).size()
batsmenMatchByMatchData['6s'] = batsmenMatchByMatchData['6s'].fillna(0)
batsmenMatchByMatchData['4s'] = batsmenMatchByMatchData['4s'].fillna(0)
batsmenMatchByMatchData['Strike_Rate'] = (
    batsmenMatchByMatchData['Total_Runs'] / batsmenMatchByMatchData['Balls_Faced']) * 100
batsmenMatchByMatchData['ducks'] = batsmenMatchByMatchData.apply(
    lambda x: 1 if ((x['Total_Runs'] == 0.0) & (x['Dismissal'] == 1.0)) else 0, axis=1
)

batsmenMatchByMatchData["dream 11 score"] = (
    (batsmenMatchByMatchData['ducks']*-2) +
    (batsmenMatchByMatchData['Total_Runs']) +
    (batsmenMatchByMatchData['4s'] * 1) +
    (batsmenMatchByMatchData['6s'] * 2) +
    (batsmenMatchByMatchData['30'] * 4) +
    (batsmenMatchByMatchData['50'] * 8) +
    (batsmenMatchByMatchData['100'] * 16) +
    ((batsmenMatchByMatchData['Strike_Rate'] >= 170) * 6) +
    ((150 <= batsmenMatchByMatchData['Strike_Rate']) & (batsmenMatchByMatchData['Strike_Rate'] < 170) * 4) +
    ((130 <= batsmenMatchByMatchData['Strike_Rate']) & (batsmenMatchByMatchData['Strike_Rate'] < 150) * 2) +
    ((60 <= batsmenMatchByMatchData['Strike_Rate']) & (batsmenMatchByMatchData['Strike_Rate'] < 70) * -2) +
    ((50 <= batsmenMatchByMatchData['Strike_Rate']) & (batsmenMatchByMatchData['Strike_Rate'] < 60) * -4) +
    (batsmenMatchByMatchData['Strike_Rate'] >= 12) * -6
)
batsmenMatchByMatchData.reset_index(inplace=True)
batsmenMatchByMatchData.to_csv('batsmenMatchByMatchData.csv', index=False)
