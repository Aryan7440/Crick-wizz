import pandas as py
import numpy as np
import matplotlib as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.metrics import r2_score
from sklearn.ensemble import ExtraTreesRegressor
df = py.read_csv(r'D:\ML\BTP\final\final_batsmen.csv')


le = LabelEncoder()
df['striker'] = le.fit_transform(df['striker'])
df['venue'] = le.fit_transform(df['venue'])
df['bowling_team'] = le.fit_transform(df['bowling_team'])


y = df.pop('dream 11 score')
X = df
# X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
extra_trees = ExtraTreesRegressor(n_estimators=100,
                                  criterion='friedman_mse', max_features="auto")
extra_trees.fit(X, y)
y_pred = extra_trees.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


r2 = r2_score(y_test, y_pred)
print("r2 is:", r2)
