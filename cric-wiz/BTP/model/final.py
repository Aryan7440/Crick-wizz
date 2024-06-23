from pycaret.regression import *
import pandas as py
import numpy as np
import matplotlib as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score, mean_squared_error
import scipy.stats as stats
from sklearn.ensemble import ExtraTreesRegressor
df = py.read_csv(r'D:\ML\BTP\model\final_batsmen.csv')
df.drop('match_id', axis=1, inplace=True)
le = LabelEncoder()


df['striker'] = le.fit_transform(df['striker'])
df['venue'] = le.fit_transform(df['venue'])
df['bowling_team'] = le.fit_transform(df['bowling_team'])


# exp = setup(data=df, target='dream 11 score')
# best_models = compare_models()
# py.set_option('display.max_columns', None)

# scaler = StandardScaler()
# # fit and transform the data
# X = scaler.fit_transform(X)


y = df.pop('dream 11 score')
X = df
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

extra_trees = ExtraTreesRegressor()

# Define the hyperparameters for tuning
param_dist = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2'],
    'bootstrap': [True, False]
}

# Perform random search with cross-validation
# random_search = RandomizedSearchCV(
#     extra_trees, param_distributions=param_dist, n_iter=100, cv=3, scoring='neg_mean_squared_error')
# random_search.fit(X_train, y_train)

# # Best parameters found by RandomizedSearchCV
# best_params = random_search.best_params_
# print("Best Parameters:", best_params)

# Use the best model for prediction
# best_extra_trees = random_search.best_estimator_
# y_pred = best_extra_trees.predict(X_test)

# Metrics
# mse = mean_squared_error(y_test, y_pred)
# print("Mean Squared Error:", mse)
# best_params={'n_estimators': 300, 'min_samples_split': 2, 'min_samples_leaf': 2,
#     'max_features': 'auto', 'max_depth': 5, 'bootstrap': True}
