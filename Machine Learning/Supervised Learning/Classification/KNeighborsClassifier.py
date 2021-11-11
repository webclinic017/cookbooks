# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:16:23 2021

@author: LK
"""

from sklearn import datasets
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Import the iris-dataset from sklearn

iris = datasets.load_iris()

# Extraxt the relevant data from the bunch

iris_df = pd.DataFrame(iris['data'])
iris_df['class'] = iris['target']

# Assign column names

iris_df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']

# Create variables for the features and the response variable

y = iris_df['class']
X = iris_df.drop('class', axis=1)

# Split into training and test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42, stratify=y)

# Create a k-NN classifier with 6 neighbors

knn = KNeighborsClassifier(n_neighbors = 5)

# Fit the classifier to the data

knn.fit(X_test, y_test)

# Compute the accuracy of the classifiers prediction using the score() method

print(knn.score(X_test, y_test))












