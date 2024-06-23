from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# You can replace with your desired regression model
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Sample data (replace with your own dataset)
data = pd.read_csv(r'..\preprocessing\batsmenMatchByMatchData.csv')
data.drop('match_id', axis=1)

label_encoder = LabelEncoder()

# Encode categorical features
# data['striker'] = label_encoder.fit_transform(data['striker'])
# data['venue'] = label_encoder.fit_transform(data['venue'])
# data['bowling_team'] = label_encoder.fit_transform(
#     data['bowling_team'])
# Define your features and target variables
features = data[['striker', 'venue', 'bowling_team']]
# Define all target variables
targets = data[['Total_Runs', 'Dismissal', 'Strike_Rate', 'Balls_Faced']]
targets['Dismissal'] = targets['Dismissal'].fillna(0)

X_train, X_test, y_train, y_test = train_test_split(
    features, targets, test_size=0.2, random_state=42)

model = ExtraTreesRegressor(n_estimators=100, max_depth=6, random_state=42)
model.fit(X_train, y_train)
etr_predictions = model.predict(X_test)
extratrees_mse = mean_squared_error(y_test, etr_predictions)
extratrees_r2 = r2_score(y_test, etr_predictions)


# player='Shubman Gill'
# stadium='M Chinnaswamy Stadium, Bengaluru'
# opposition='Royal Challengers Bangalore'
