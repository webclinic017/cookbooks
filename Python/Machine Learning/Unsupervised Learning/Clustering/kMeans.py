# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:26:18 2021

@author: LK
"""

from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Load data

iris_data = datasets.load_iris()

# Extract features and labels from bunch 

features_df = pd.DataFrame(iris_data['data'], columns=iris_data['feature_names'])
labels_df = pd.DataFrame(iris_data['target'], columns=['label'])

# Create np.arrays

features_np = np.array(features_df)
labels_np = np.array(labels_df)

# Create scaler 

scaler = StandardScaler()

# Create kMeans Instance with 3 clusters

kmeans = KMeans(n_clusters=3)

# Create a pipeline

pipeline = make_pipeline(scaler, kmeans)

# Fit the pipelines to sample 

pipeline.fit(features_np)

# Calculate the predictions

pred_labels = pipeline.predict(features_np)

# Create a dataframe to compare the predicted data with the labels

compare_df = pd.DataFrame()
compare_df['Pred Labels'] = pred_labels
compare_df['Labels'] = labels_np

# Create crosstab

ct = pd.crosstab(compare_df['Pred Labels'], compare_df['Labels'])
print(ct)



