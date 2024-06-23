import numpy as np
import pandas as py
import pickle
with open(r'D:\BTP flask\batter\striker_encoder.pkl', 'rb') as file:
    st = pickle.load(file)
with open(r'D:\BTP flask\batter\venue_encoder.pkl', 'rb') as file:
    vn = pickle.load(file)
with open(r'D:\BTP flask\batter\bowling_team_encoder.pkl', 'rb') as file:
    op = pickle.load(file)


batsmen_data = py.read_csv(r'D:\ML\BTP\jupyter\batsmenData.csv')
batsmenOppositiondata = py.read_csv(
    r'D:\ML\BTP\jupyter\batsmenOppositionWiseData.csv')
batsmenVenue = py.read_csv(
    r'D:\ML\BTP\jupyter\batsmenVenueWiseData.csv')

venueData = py.read_csv(
    r'D:\ML\BTP\jupyter\VenueData.csv')





def input_Data(batsmen, venue, opposotion):


    Avg_balls_faced=0
    Matches_Played=0
    Strike_Rate=0
    Average=0
    avg_drm11_score=0
    if(batsmen_data[batsmen_data['striker']== batsmen].empty==False):
        Avg_balls_faced = batsmen_data[batsmen_data['striker']
                                    == batsmen]['Avg_balls_faced'].values[0]
        Matches_Played = batsmen_data[batsmen_data['striker']
                                    == batsmen]['Matches_Played'].values[0]
        Strike_Rate = batsmen_data[batsmen_data['striker']
                                == batsmen]['Strike_Rate'].values[0]
        Average = batsmen_data[batsmen_data['striker']
                            == batsmen]['Average'].values[0]
        avg_drm11_score = batsmen_data[batsmen_data['striker']
                                    == batsmen]['avg_drm11_score'].values[0]
    
    opposition_wise_Matches_Played=0
    opposition_wiseStrike_Rate=0
    opposition_wiseAverage=0
    opposition_wise_dr11=0
    
    if (batsmenOppositiondata[(batsmenOppositiondata['striker'] == batsmen) & (batsmenOppositiondata['bowling_team'] == opposotion)].empty):
        opposition_wise_Matches_Played = batsmenOppositiondata.groupby(
            ['bowling_team'])['opposition_wise_Matches_Played'].mean()[opposotion]
        opposition_wiseStrike_Rate = batsmenOppositiondata.groupby(
            ['bowling_team'])['opposition_wise_Matches_Played'].mean()[opposotion]
        opposition_wiseAverage = batsmenOppositiondata.groupby(
            ['bowling_team'])['opposition_wise_Matches_Played'].mean()[opposotion]
        opposition_wise_dr11 = batsmenOppositiondata.groupby(
            ['bowling_team'])['opposition_wise_Matches_Played'].mean()[opposotion]
    
    else:
        opposition_wise_Matches_Played = batsmenOppositiondata[(batsmenOppositiondata['striker']
                                                                == batsmen) & (batsmenOppositiondata['bowling_team'] == opposotion)]['opposition_wise_Matches_Played'].values[0]
        opposition_wiseStrike_Rate = batsmenOppositiondata[(batsmenOppositiondata['striker']
                                                            == batsmen) & (batsmenOppositiondata['bowling_team'] == opposotion)]['opposition_wiseStrike_Rate'].values[0]
        opposition_wiseAverage = batsmenOppositiondata[(batsmenOppositiondata['striker']
                                                        == batsmen) & (batsmenOppositiondata['bowling_team'] == opposotion)]['opposition_wiseAverage'].values[0]
        opposition_wise_dr11 = batsmenOppositiondata[(batsmenOppositiondata['striker']
                                                    == batsmen) & (batsmenOppositiondata['bowling_team'] == opposotion)]['opposition_wise_dr11'].values[0]
    
    
    
    
    
    
    
    
    
    
    
    # opposition_wise_Matches_Played = batsmenOppositiondata[(batsmenOppositiondata['striker']
    #                                                         == batsmen) & (batsmenOppositiondata['bowling_team'] == opposotion)]['opposition_wise_Matches_Played'].values[0]
    # opposition_wiseStrike_Rate = batsmenOppositiondata[(batsmenOppositiondata['striker']
    #                                                     == batsmen) & (batsmenOppositiondata['bowling_team'] == opposotion)]['opposition_wiseStrike_Rate'].values[0]
    # opposition_wiseAverage = batsmenOppositiondata[(batsmenOppositiondata['striker']
    #                                                 == batsmen) & (batsmenOppositiondata['bowling_team'] == opposotion)]['opposition_wiseAverage'].values[0]
    # opposition_wise_dr11 = batsmenOppositiondata[(batsmenOppositiondata['striker']
    #                                               == batsmen) & (batsmenOppositiondata['bowling_team'] == opposotion)]['opposition_wise_dr11'].values[0]
    batsmen_venueWise_Matches_Played=0
    batsmen_venueWise_Strike_Rate=0
    batsmen_venueWise_Average=0
    batsmen_venueWise_dr11=0
    if (batsmenVenue[(batsmenVenue['striker']
                     == batsmen) & (batsmenVenue['venue'] == venue)].empty):
        batsmen_venueWise_Matches_Played=batsmenVenue.groupby(['venue'])['venueWise_Matches_Played'].mean()[venue]
        batsmen_venueWise_Strike_Rate=batsmenVenue.groupby(['venue'])['venueWise_Strike_Rate'].mean()[venue]
        batsmen_venueWise_Average=batsmenVenue.groupby(['venue'])['venueWise_Average'].mean()[venue]
        batsmen_venueWise_dr11=batsmenVenue.groupby(['venue'])['venueWise_dr11'].mean()[venue]
    else:
        batsmen_venueWise_Matches_Played = batsmenVenue[(batsmenVenue['striker']
                                                    == batsmen) & (batsmenVenue['venue'] == venue)]['venueWise_Matches_Played'].values[0]
        batsmen_venueWise_Strike_Rate = batsmenVenue[(batsmenVenue['striker']
                                                    == batsmen) & (batsmenVenue['venue'] == venue)]['venueWise_Strike_Rate'].values[0]
        batsmen_venueWise_Average = batsmenVenue[(batsmenVenue['striker']
                                                == batsmen) & (batsmenVenue['venue'] == venue)]['venueWise_Average'].values[0]
        batsmen_venueWise_dr11 = batsmenVenue[(batsmenVenue['striker']
                                            == batsmen) & (batsmenVenue['venue'] == venue)]['venueWise_dr11'].values[0]
        

    # batsmen_venueWise_Matches_Played = batsmenVenue[(batsmenVenue['striker']
    #                                                 == batsmen) & (batsmenVenue['venue'] == venue)]['venueWise_Matches_Played'].values[0]
    # batsmen_venueWise_Strike_Rate = batsmenVenue[(batsmenVenue['striker']
    #                                               == batsmen) & (batsmenVenue['venue'] == venue)]['venueWise_Strike_Rate'].values[0]
    # batsmen_venueWise_Average = batsmenVenue[(batsmenVenue['striker']
    #                                           == batsmen) & (batsmenVenue['venue'] == venue)]['venueWise_Average'].values[0]
    # batsmen_venueWise_dr11 = batsmenVenue[(batsmenVenue['striker']
    #                                        == batsmen) & (batsmenVenue['venue'] == venue)]['venueWise_dr11'].values[0]

    Venue_Matches_Played = venueData[venueData['venue']
                                     == venue]['Venue_Matches_Played'].values[0]
    Venue_Avg_Batsmen_Strike_Rate = venueData[venueData['venue']
                                              == venue]['Venue_Avg_Batsmen_Strike_Rate'].values[0]
    Venue_Avg_Batsmen_Average = venueData[venueData['venue']
                                          == venue]['Venue_Avg_Batsmen_Average'].values[0]
    Venue_Avg_Bowler_Economy = venueData[venueData['venue']
                                         == venue]['Venue_Avg_Bowler_Economy'].values[0]
    Venue_Avg_Bowler_Average = venueData[venueData['venue']
                                         == venue]['Venue_Avg_Bowler_Average'].values[0]
    Venue_dream11 = venueData[venueData['venue']
                              == venue]['Venue_dream11'].values[0]
    bat = [1]
    ven = vn.transform([venue])
    oppo = op.transform([opposotion])
    if batsmen in st.classes_:
        bat = st.transform([batsmen])
    data = np.array([[bat[0], ven[0], oppo[0], Avg_balls_faced, Matches_Played,	Strike_Rate,	Average, avg_drm11_score,	opposition_wise_Matches_Played, opposition_wiseStrike_Rate,	opposition_wiseAverage,	opposition_wise_dr11,	batsmen_venueWise_Matches_Played,
                    batsmen_venueWise_Strike_Rate,	batsmen_venueWise_Average,	batsmen_venueWise_dr11,	Venue_Matches_Played,	Venue_Avg_Batsmen_Strike_Rate,	Venue_Avg_Batsmen_Average,	Venue_Avg_Bowler_Economy,	Venue_Avg_Bowler_Average,	Venue_dream11]])
    # print(loaded_model.predict(data))
    return data
