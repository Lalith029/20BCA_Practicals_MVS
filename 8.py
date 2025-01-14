# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 10:41:07 2022

@author: Lalith
"""

import os
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering 
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage

os.chdir("C:/Users/Master/Desktop/Datasets")
df = pd.read_csv("shopping_data.csv")
df.head()
df.info()
genre = pd.get_dummies(df['Genre'])
df.drop(['Genre'],axis=1,inplace=True)
df = pd.concat([df,genre],axis=1)
df.info()
df=np.array(df)

Z = linkage(df, method = "ward") 
dendro = dendrogram(Z) 
plt.title('Dendogram') 
plt.ylabel('Euclidean distance') 
plt. show()

ac=AgglomerativeClustering(n_clusters=2,affinity="euclidean",linkage="ward") 
labels=ac.fit_predict(df) 
plt.figure(figsize = (8,5)) 
plt.scatter(df[labels == 0,0], df[labels == 0,1], c='red')
plt.scatter(df[labels == 1,0], df[labels == 1,1], c='blue') 
plt.scatter(df[labels == 2,0], df[labels == 2,1], c='green') 
plt.scatter(df[labels == 3,0], df[labels == 3,1], c='black') 
plt.scatter(df[labels == 4,0], df[labels == 4,1], c='orange') 
plt.show()