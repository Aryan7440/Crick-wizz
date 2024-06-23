from flask import Flask, request, render_template
import numpy as np
import pandas as py
from greedy_knapsack import *
from features_eng import *
from predictoin_module import *
from teams_list import *
from features_eng_bowl import *

app = Flask(__name__, static_url_path='/static')




@app.route('/')
def home():
    return render_template('index.html')




@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        team_name = request.form['team_name']
        opposition = request.form['team2']
        venue = request.form['venue']
        player_info=predict_player_points(team_name,opposition,venue)
        total,selected_players=select_players_for_team(player_info)
        return render_template('result.html', team=team_name, players=selected_players)


if __name__ == '__main__':
    app.run(debug=True)
