# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 06:22:17 2022

@author: Lalith
"""

import numpy as np
X=np.array([1,2,3,4,5,6,7])
print(X)

# 2nd, 4th and 7th element of an array
X=np.array([1,2,3,4,5,6,7,8,9,12]) 
print(X[1])
print(X[3])
print(X[6])
#3
# shape of an array
X=np.array([[1,2,3,4],[5,6,7,8]])
print(X.shape)
#4
#transpose
X=np.array([[1,2,3,4],[5,6,7,8]]).T
print(X)
#5          
# 4*5 vector matrix
X=np.array([[1,2,3,4,5],[5,6,7,8,9],[3,5,6,7,8],[1,4,5,6,7]])
print(X)
#6
# shape of the above matrix
X=np.array([[1,2,3,4,5],[5,6,7,8,9],[3,5,6,7,8],[1,4,5,6,7]])
print(np.shape(X))
#7
# transpose of this matrix
X=np.array([[1,2,3,4,5],[5,6,7,8,9],[3,5,6,7,8],[1,4,5,6,7]]).T
print(X)
#8
#print the first column of the matrix
X=np.array([[1,2,3,4,5],[5,6,7,8,9],[3,5,6,7,8],[1,4,5,6,7]])
print("First column")
#9
#print the first row of the matrix
print(X[:,0])
print("First row")
print(X[0])
#10
#create 7 dimensional array with only 0s, create a 3 dimensional array with only 1s
print(np.zeros(7))
print(np.ones(3))