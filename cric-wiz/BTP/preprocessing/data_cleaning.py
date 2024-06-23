import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\data\ipl_male_csv2\all_matches.csv')
# df['Dismissal'].fillna(0, inplace=True)
df['Dismissal'] = df.apply(lambda row: 1 if py.notna(
    row['player_dismissed']) else 0, axis=1)
df['season'] = py.to_datetime(df['start_date'].str[:4], format='%Y')
df['player_dismissed'] = df.apply(lambda row: 1 if py.notna(
    row['player_dismissed']) else np.nan, axis=1)
# df['season'] = py.to_datetime(df['start_date'].str[:4], format='%Y')
df['venue'] = df['venue'].str.replace(r',.*', '', regex=True)
replacement_dict = {
    'Feroz Shah Kotla': 'Arun Jaitley Stadium',
    'M.Chinnaswamy Stadium': 'M Chinnaswamy Stadium',
    'Sardar Patel Stadium': 'Narendra Modi Stadium',
    'Punjab Cricket Association IS Bindra Stadium': 'Punjab Cricket Association Stadium'}
df['venue'] = df['venue'].replace(replacement_dict)
df['noballs'].fillna(0, inplace=True)
df['wides'].fillna(0, inplace=True)
df['byes'].fillna(0, inplace=True)
df['legbyes'].fillna(0, inplace=True)
df['penalty'].fillna(0, inplace=True)
df['wicket_type'].fillna(0, inplace=True)
df['player_dismissed'].fillna(0, inplace=True)
df['other_wicket_type'].fillna(0, inplace=True)
df['other_player_dismissed'].fillna(0, inplace=True)
df.to_csv('all_matches.csv', index=False)
