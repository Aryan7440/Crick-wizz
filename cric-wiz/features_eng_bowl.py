import pandas as py
import numpy as np

import pickle

bowlerData=py.read_csv(r'D:\ML\BTP\preprocessing\bowlerData.csv')
bowlerOPP=py.read_csv(r'D:\ML\BTP\preprocessing\bowlerOppositionWiseData.csv')
bowlerVenue=py.read_csv(r'D:\ML\BTP\preprocessing\bowlerVenueWiseData.csv')
venueData=py.read_csv(r'D:\ML\BTP\preprocessing\VenueData.csv')

# bowler='Mohammed Shami'
# venue='Narendra Modi Stadium'
# oppposition='Chennai Super Kings'

with open(r'D:\BTP flask\bowler\bowler_encoder.pkl', 'rb') as file:
    bw = pickle.load(file)
with open(r'D:\BTP flask\bowler\venue_encoder.pkl', 'rb') as file:
    vn = pickle.load(file)
with open(r'D:\BTP flask\bowler\batting_team_encoder.pkl', 'rb') as file:
    bt = pickle.load(file)
def bowler_input(bowler,venue,oppposition):

    Matches_Played=0
    avg_drm11_score=0
    strike_rate=0
    Economy=0
    if(bowlerData[bowlerData['bowler']==bowler].empty==False):
        Matches_Played=bowlerData[bowlerData['bowler']==bowler]['Matches_Played'].values[0]
        avg_drm11_score=bowlerData[bowlerData['bowler']==bowler]['avg_drm11_score'].values[0]
        Economy=bowlerData[bowlerData['bowler']==bowler]['Economy'].values[0]
        strike_rate=bowlerData[bowlerData['bowler']==bowler]['strike_rate'].values[0]


    bowlerOppositionWiseMatches_Played=0
    bowlerOppositionWiseavg_drm11_score=0
    bowlerOppositionWiseEconomy=0
    bowlerOppositionWisestrike_rate=0
    if(bowlerOPP[(bowlerOPP['bowler']==bowler) & (bowlerOPP['batting_team']==oppposition)].empty):  
        bowlerOppositionWiseMatches_Played=bowlerOPP.groupby(['batting_team'])['bowlerOppositionWiseMatches_Played'].mean()[oppposition]
        bowlerOppositionWiseavg_drm11_score=bowlerOPP.groupby(['batting_team'])['bowlerOppositionWiseavg_drm11_score'].mean()[oppposition]
        bowlerOppositionWiseEconomy=bowlerOPP.groupby(['batting_team'])['bowlerOppositionWiseEconomy'].mean()[oppposition]
        bowlerOppositionWisestrike_rate=bowlerOPP.groupby(['batting_team'])['bowlerOppositionWisestrike_rate'].mean()[oppposition]
    else:
        bowlerOppositionWiseMatches_Played=bowlerOPP[(bowlerOPP['bowler']==bowler) & (bowlerOPP['batting_team']==oppposition)]['bowlerOppositionWiseMatches_Played'].values[0]
        bowlerOppositionWiseavg_drm11_score=bowlerOPP[(bowlerOPP['bowler']==bowler) & (bowlerOPP['batting_team']==oppposition)]['bowlerOppositionWiseavg_drm11_score'].values[0]
        bowlerOppositionWiseEconomy=bowlerOPP[(bowlerOPP['bowler']==bowler) & (bowlerOPP['batting_team']==oppposition)]['bowlerOppositionWiseEconomy'].values[0]
        bowlerOppositionWisestrike_rate=bowlerOPP[(bowlerOPP['bowler']==bowler) & (bowlerOPP['batting_team']==oppposition)]['bowlerOppositionWisestrike_rate'].values[0]        
    bowlerVenueMatches_Played=0
    bowlerVenueavg_drm11_score=0
    bowlerVenueEconomy=0
    bowlerVenuestrike_rate=0
    if(bowlerVenue[(bowlerVenue['bowler']==bowler) & (bowlerVenue['venue']==venue)].empty):
        bowlerVenueMatches_Played=bowlerVenue.groupby(['venue'])['bowlerVenueMatches_Played'].mean()[venue]
        bowlerVenueavg_drm11_score=bowlerVenue.groupby(['venue'])['bowlerVenueavg_drm11_score'].mean()[venue]
        bowlerVenueEconomy=bowlerVenue.groupby(['venue'])['bowlerVenueEconomy'].mean()[venue]
        bowlerVenuestrike_rate=bowlerVenue.groupby(['venue'])['bowlerVenuestrike_rate'].mean()[venue]
    else:
        bowlerVenueMatches_Played=bowlerVenue[(bowlerVenue['bowler']==bowler) & (bowlerVenue['venue']==venue)]['bowlerVenueMatches_Played'].values[0]
        bowlerVenueavg_drm11_score=bowlerVenue[(bowlerVenue['bowler']==bowler) & (bowlerVenue['venue']==venue)]['bowlerVenueavg_drm11_score'].values[0]
        bowlerVenueEconomy=bowlerVenue[(bowlerVenue['bowler']==bowler) & (bowlerVenue['venue']==venue)]['bowlerVenueEconomy'].values[0]
        bowlerVenuestrike_rate=bowlerVenue[(bowlerVenue['bowler']==bowler) & (bowlerVenue['venue']==venue)]['bowlerVenuestrike_rate'].values[0]
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
    
    bow = [2]
    ven = vn.transform([venue])
    oppo = bt.transform([oppposition])
    
    
    if bowler in bw.classes_:
        bow = bw.transform([bowler])
    if venue in vn.classes_:
        ven = vn.transform([venue])
    if oppposition in bw.classes_:
        oppo = bt.transform([oppposition])

    data = np.array([[bow[0], ven[0], oppo[0], Matches_Played, avg_drm11_score,Economy,	strike_rate,	bowlerOppositionWiseMatches_Played, bowlerOppositionWiseavg_drm11_score,	bowlerOppositionWiseEconomy, bowlerOppositionWisestrike_rate,	bowlerVenueMatches_Played,	bowlerVenueavg_drm11_score,	bowlerVenueEconomy,
                    bowlerVenuestrike_rate,Venue_Matches_Played,	Venue_Avg_Batsmen_Strike_Rate,	Venue_Avg_Batsmen_Average,	Venue_Avg_Bowler_Economy,	Venue_Avg_Bowler_Average,	Venue_dream11]])
    return data