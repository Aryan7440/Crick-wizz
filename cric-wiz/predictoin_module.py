import numpy as np
import pandas as py
import pickle
from features_eng import *
from features_eng_bowl import *
from teams_list import *

model1_et = pickle.load(open(r'D:\BTP flask\batter\et.pkl', 'rb'))
model1_cat = pickle.load(open(r'D:\BTP flask\batter\cat.pkl', 'rb'))
model1_xgb = pickle.load(open(r'D:\BTP flask\batter\xgb.pkl', 'rb'))


model2_et=pickle.load(open(r'D:\BTP flask\bowler\et.pkl', 'rb'))
model2_cat=pickle.load(open(r'D:\BTP flask\bowler\cat.pkl', 'rb'))
model2_xgb=pickle.load(open(r'D:\BTP flask\bowler\xgb.pkl', 'rb'))


def predict_player_points(team1,team2, venue):
    player_points = []

    for player,role in teams[team1]:
            if role == 'batter' or role == 'wicket_keeper' :
                points = (model1_et.predict(input_Data(player, venue, team2))[0]+model1_cat.predict(input_Data(player, venue, team2))[0]+model1_xgb.predict(input_Data(player, venue, team2))[0])/3
            elif role == 'bowler':
                points = (model2_et.predict(bowler_input(player, venue, team2))[0]+model2_cat.predict(bowler_input(player, venue, team2))[0]+model2_xgb.predict(bowler_input(player, venue, team2))[0])/3
            else:
                points = (model1_et.predict(input_Data(player, venue, team2))[0]+model1_cat.predict(input_Data(player, venue, team2))[0]+model1_xgb.predict(input_Data(player, venue, team2))[0])/3  + (model2_et.predict(bowler_input(player, venue, team2))[0]+model2_cat.predict(bowler_input(player, venue, team2))[0]+model2_xgb.predict(bowler_input(player, venue, team2))[0])/3
            player_points.append((player, role, team1, points))
    for player,role in teams[team2]:
            if role == 'batter' or role == 'wicket_keeper':
                points = (model1_et.predict(input_Data(player, venue, team2))[0]+model1_cat.predict(input_Data(player, venue, team2))[0]+model1_xgb.predict(input_Data(player, venue, team2))[0])/3
            elif role == 'bowler':
                points = (model2_et.predict(bowler_input(player, venue, team2))[0]+model2_cat.predict(bowler_input(player, venue, team2))[0]+model2_xgb.predict(bowler_input(player, venue, team2))[0])/3
            else:
                points = (model1_et.predict(input_Data(player, venue, team2))[0]+model1_cat.predict(input_Data(player, venue, team2))[0]+model1_xgb.predict(input_Data(player, venue, team2))[0])/3  + (model2_et.predict(bowler_input(player, venue, team2))[0]+model2_cat.predict(bowler_input(player, venue, team2))[0]+model2_xgb.predict(bowler_input(player, venue, team2))[0])/3
            player_points.append((player, role, team2, points))
    return player_points


# Example usage
# team1_name = 'Chennai Super Kings'
# team2_name = 'Gujarat Titans'
# predicted_player_points = predict_player_points(
#     team1_name, team2_name, 'Narendra Modi Stadium')
# print(predicted_player_points)

