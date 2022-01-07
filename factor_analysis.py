# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:27:25 2022

@author: tejas
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import FactorAnalysis
from sklearn import preprocessing
mydata=pd.read_csv("C:/Users/tejas/Documents/jerry(DS)/datasets/Walmart_Store_sales.csv")
print(mydata.drop('Date',axis=1,inplace=True))
print(mydata.shape)
print(mydata.head(10))
mydata.info()
print(mydata.describe())
print(mydata.dtypes)
data_normal = preprocessing.scale(mydata)
fa = FactorAnalysis(n_components = 1)
fa.fit(data_normal)
for score in fa.score_samples(data_normal):
    print(score) 