def select_players_for_team(players):

    players = sorted(players, key=lambda x: x[3], reverse=True)

    selected_players = {'wicket_keeper': [], 'batter': [], 'bowler': [], 'all_rounder': []}
    total_points = 0
    
    for player in players:
        if ((len(selected_players['wicket_keeper']) ==1) and (len(selected_players['batter']) == 4)
                and (len(selected_players['bowler'])) ==4 and (len(selected_players['all_rounder']) ==1)):
            selected_players['wicket_keeper'].append(player)
            total_points += player[3]
            break

        role = player[1]
        team=player[2]
        if role == 'wicket_keeper' and len(selected_players['wicket_keeper']) == 0:
            selected_players['wicket_keeper'].append(player)
            total_points += player[3]
        elif role == 'batter' and len(selected_players['batter']) < 4:
            selected_players['batter'].append(player)
            total_points += player[3]
        elif role == 'bowler' and len(selected_players['bowler']) < 4:
            selected_players['bowler'].append(player)
            total_points += player[3]
        elif role == 'all_rounder' and len(selected_players['all_rounder']) == 0:
            selected_players['all_rounder'].append(player)
            total_points += player[3]
    total_players=[]
    total_players+=selected_players['all_rounder']
    total_players+=selected_players['bowler']
    total_players+=selected_players['batter']
    total_players+=selected_players['wicket_keeper']
    return total_points, total_players
    # return 10,players

# # Example usage:
# players_array = [
#     ("Player1", "role1", "TeamA", 100),
#     ("Player2", "role2", "TeamB", 90),
#     # Add more players here
# ]

# max_points, selected_players = select_players_for_team(players_array)

# print("Maximum Total Points:", max_points)
# print("Selected Players:", selected_players)
