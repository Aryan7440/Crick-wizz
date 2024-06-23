import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\preprocessing\all_matches.csv')
df['player_dismissed'] = df.apply(lambda row: row['bowler'] if py.notna(
    row['player_dismissed']) else np.nan, axis=1)
df['season'] = py.to_datetime(df['start_date'].str[:4], format='%Y')
df['venue'] = df['venue'].str.replace(r',.*', '', regex=True)
replacement_dict = {
    'Feroz Shah Kotla': 'Arun Jaitley Stadium',
    'M.Chinnaswamy Stadium': 'M Chinnaswamy Stadium',
    'Sardar Patel Stadium': 'Narendra Modi Stadium',
    'Punjab Cricket Association IS Bindra Stadium': 'Punjab Cricket Association Stadium'}
df['venue'] = df['venue'].replace(replacement_dict)
MatchData = df.groupby(['match_id', 'season', 'venue']).agg(
    Total_Runs=py.NamedAgg(column='runs_off_bat', aggfunc='sum'),
    Total_Extras=py.NamedAgg(column='extras', aggfunc='sum'),
    Wickets_Taken=py.NamedAgg(
        column='Dismissal', aggfunc='sum'),
    balls_bowled=py.NamedAgg(column='bowler', aggfunc='size')
)
bat_data = py.read_csv(r'D:\ML\BTP\preprocessing\batsmenMatchByMatchData.csv')
MatchData['100s'] = bat_data.groupby('match_id')['100'].sum().values
MatchData['50s'] = bat_data.groupby('match_id')['50'].sum().values
MatchData['30s'] = bat_data.groupby('match_id')['30'].sum().values
MatchData['sixes'] = bat_data.groupby('match_id')['6s'].sum().values
MatchData['fours'] = bat_data.groupby('match_id')['4s'].sum().values
MatchData['ducks'] = bat_data.groupby('match_id')['ducks'].sum().values
MatchData['d11'] = bat_data.groupby('match_id')['dream 11 score'].sum().values

MatchData.reset_index(inplace=True)
MatchData.to_csv('MatchData.csv', index=False)
