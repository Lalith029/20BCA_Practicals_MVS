# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 06:40:07 2022

@author: Lalith
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.chdir("C:/Users/Lalith/Desktop/Python")
data1=pd.read_csv('Telecom_Data.csv')
print(data1.head())
print(data1.describe())
print(data1)
sns.countplot(x ='area code', data= data1)
plt.show()
sns.scatterplot(x ='total day charge',y ='total day calls',hue='area code',data =data1)
plt.show()
sns.pairplot(data1.drop(['number vmail messages'],axis=1),hue='area code',height=3)
plt.show()
X=data1.corr(method='pearson')
print(X)
sns.heatmap(data1.corr(method='pearson').drop(['total intl calls'],axis=1).drop(['total intl calls'],axis=0))
plt.show()
sns.boxplot(x="total intl calls",y="total intl charge",data=data1)
plt.show()
