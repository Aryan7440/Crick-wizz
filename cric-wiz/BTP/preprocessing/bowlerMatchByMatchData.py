from sklearn.preprocessing import LabelEncoder
import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\preprocessing\all_matches.csv')
df['player_dismissed'] = df.apply(lambda row: row['bowler'] if py.notna(
    row['player_dismissed']) else np.nan, axis=1)
df['season'] = py.to_datetime(df['start_date'].str[:4], format='%Y')


le = LabelEncoder()
cat = le.fit(df["wicket_type"])
types = cat.classes_
cat.transform(types)
df["WType"] = cat.transform(df["wicket_type"])

df['GW'] = df['WType'].apply(lambda row: 1 if row in [0, 2, 3, 4, 9] else 0)

bowlerMatchByMatchData = df.groupby(['match_id', 'bowler', 'venue', 'batting_team']).agg(
    Runs_Conceded=py.NamedAgg(column='runs_off_bat', aggfunc='sum'),
    Wickets_Taken=py.NamedAgg(
        column='Dismissal', aggfunc='sum'),
    Good_wickets=py.NamedAgg(
        column='GW', aggfunc='sum'),
    balls_bowled=py.NamedAgg(column='bowler', aggfunc='size')
)

bowlerMatchByMatchData['5ws'] = bowlerMatchByMatchData['Wickets_Taken'].apply(
    lambda x: 1 if x >= 5 else 0
)
bowlerMatchByMatchData['3ws'] = bowlerMatchByMatchData['Wickets_Taken'].apply(
    lambda x: 1 if x == 3 else 0
)
bowlerMatchByMatchData['4ws'] = bowlerMatchByMatchData['Wickets_Taken'].apply(
    lambda x: 1 if x == 4 else 0
)
bowlerMatchByMatchData['Economy'] = (
    (bowlerMatchByMatchData['Runs_Conceded']*6)/(bowlerMatchByMatchData['balls_bowled']))
bowlerMatchByMatchData['strike_rate'] = bowlerMatchByMatchData.apply(
    lambda row: row['balls_bowled'] / row['Wickets_Taken'] if row['Wickets_Taken'] != 0 else row['balls_bowled']+20, axis=1
)

maiden_overs = []

# Group data by 'Bowler' and 'Match'
grouped_data = df.groupby(['match_id', 'bowler', 'batting_team'])

for group, group_df in grouped_data:
    match, bowler, team = group
    deliveries = group_df['runs_off_bat']
    # Count the number of maiden overs in the match
    maiden_over_count = 0
    consecutive_dot_balls = 0

    for delivery in deliveries:
        if delivery == 0:  # A dot ball
            consecutive_dot_balls += 1
            if consecutive_dot_balls == 6:  # Six consecutive dot balls make a maiden over
                maiden_over_count += 1
        else:
            consecutive_dot_balls = 0

    maiden_overs.append({'bowler': bowler, 'match_id': match,
                        'Maiden_Overs': maiden_over_count})

maiden_overs_df = py.DataFrame(maiden_overs)
bowlerMatchByMatchData.reset_index(inplace=True)
bowlerMatchByMatchData['maidens'] = maiden_overs_df['Maiden_Overs']
# Reset index
bowlerMatchByMatchData["dream 11 score"] = (
    (bowlerMatchByMatchData['Wickets_Taken'] * 25) +
    (bowlerMatchByMatchData['Good_wickets'] * 2) +
    (bowlerMatchByMatchData['4ws'] * 8) +
    (bowlerMatchByMatchData['5ws'] * 16) +
    (bowlerMatchByMatchData['maidens'] * 12) +
    ((bowlerMatchByMatchData['Economy'] < 5) * 6) +
    ((5 <= bowlerMatchByMatchData['Economy']) & (bowlerMatchByMatchData['Economy'] < 6) * 4) +
    ((6 <= bowlerMatchByMatchData['Economy']) & (bowlerMatchByMatchData['Economy'] < 7) * 2) +
    ((10 <= bowlerMatchByMatchData['Economy']) & (bowlerMatchByMatchData['Economy'] < 11) * -2) +
    ((11 <= bowlerMatchByMatchData['Economy']) & (bowlerMatchByMatchData['Economy'] < 12) * -4) +
    (bowlerMatchByMatchData['Economy'] >= 12) * -6
)

bowlerMatchByMatchData.to_csv('bowlerMatchByMatchData.csv', index=False)
