from pycaret.regression import *
import pandas as py
import numpy as np
df = py.read_csv(r'D:\ML\BTP\preprocessing\bowlerOppositionWiseData.csv')
# df.drop('match_id')

# df.drop('Wickets_Taken', axis=1)
# df.drop('balls_bowled', axis=1)
# df.drop('Matches_Played', axis=1)
# df.drop('Runs_Conceded', axis=1)
exp = setup(data=df, target='avg_drm11_score')
