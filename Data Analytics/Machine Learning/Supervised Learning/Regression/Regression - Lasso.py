# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:19:23 2021

@author: LK
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import cross_val_score
from sklearn import datasets
import matplotlib.pyplot as plt

""" 
- In normal regressions large coefficient can lead to overfitting
- With Regularization large coefficients get penalized
--> Very high alpha: Significant penalization
"""

# Import the housing data from sklearn

housing_data = datasets.load_boston()

# Extract the relevant data from the bunch

housing_df_features = pd.DataFrame(housing_data['data'])
housing_df_label = pd.DataFrame(housing_data['target'])

# Extract the feature names

housing_df_feature_names = housing_data['feature_names']

# Define feature and label

X = housing_df_features.values
y = housing_df_label.values

# Define regressor

lasso = Lasso(alpha=0.02, normalize=True)

# Fit the regressor to the data

lasso.fit(X, y)

# Compute and print the coefficients

lasso_coef = lasso.coef_
print(lasso_coef)

# Plot the coefficient

plt.plot(range(len(housing_df_features.columns)), lasso_coef)
plt.xticks(range(len(housing_df_features.columns)),housing_df_feature_names, rotation=60)
plt.show()









