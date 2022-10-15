#coding:gbk
import os
import numpy as np
from sklearn.linear_model import LinearRegression

def linear_interpolation(data, inter_num=4):
    clf = LinearRegression()
    X = np.array([[1], [inter_num+2]])
    y = data
    clf.fit(X, y)
    inter_values = clf.predict(np.array([ [i+2] for i in range(inter_num)]))
    return inter_values
    
data = [[10], [20]]
linear_interpolation(data, 1)
# array([[15.]])
def manual_linear_interpolation(x0, y0, x1, y1, x):
    return y0+(x-x0)*(y1-y0)/(x1-x0)
manual_linear_interpolation(1, 10, 3, 20, 2)
# 15.0