# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:08:38 2021

@author: LK
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn import datasets

# Import the housing data from sklearn

housing_data = datasets.load_boston()

# Extract the relevant data from the bunch

housing_df_features = pd.DataFrame(housing_data['data'])
housing_df_label = pd.DataFrame(housing_data['target'])

# Define feature and label

X = housing_df_features.values
y = housing_df_label.values

# Create the regressor

reg = LinearRegression()

# Compute 5-fold cross validation scores

cv_scores = cross_val_score(reg, X, y, cv=5)

# Print the scores

print(cv_scores)








