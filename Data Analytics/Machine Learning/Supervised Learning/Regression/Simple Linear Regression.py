# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 22:22:40 2021

@author: LK
"""

import numpy as np
import pandas as pd
from sklearn import datasets
import seaborn as sns
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Import the housing dataset from sklearn

housing_data = datasets.load_boston()

# Extract the relevant data from the bunch

housing_df = pd.DataFrame(housing_data['data'])

# Assign column names

housing_df.columns = housing_data['feature_names']

# Add the feature data

housing_df['Label'] = housing_data['target']

# Display Correlation Matrix

sns.heatmap(housing_df.corr(), square=True, cmap='RdYlGn')

# Define feature and label and split them in training- and testing-set

X_train, X_test, y_train, y_test = train_test_split(housing_df['AGE'].values.reshape(-1,1), housing_df['Label'].values.reshape(-1,1), test_size = 0.3, random_state=42)

# Create the regressor

reg = LinearRegression()

# Create the prediction space

prediction_space = np.linspace(min(X_train), max(X_train)).reshape(-1,1)

# Fit the model to the data

reg.fit(X_train, y_train)

# Compute predictions over prediction space

y_pred = reg.predict(prediction_space).reshape(-1,1)

# Print R^2

print(reg.score(X_test, y_test))

# Plot Regression Line

plt.plot(prediction_space, y_pred)
plt.show()
