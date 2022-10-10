# coding:gbk
import numpy as np
import pandas as pd
# import pandas_profiling as pp
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set(context="notebook", style="darkgrid")
import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline

from sklearn.impute import KNNImputer

data = [
    [2, 4, 8], 
    [3, np.nan, 7], 
    [5, 8, 3], 
    [4, 3, 8]
]

#��Ϊ�ڶ��������ĵ�һ������3�͵���������7�����һ�������ĵ�һ������2�͵���������8��ŷ�Ͼ������������ȱʧֵ���յ�һ����������䣬���ֵΪ4
imputer = KNNImputer(n_neighbors=1)
data1 = imputer.fit_transform(data)
print(data1)

#��ôn_neighbors=2�أ���ʱ����ŷ�Ͼ������������ڵ��ǵ�һ���������������������ʱ�����ֵ���������������ڶ�������4��3�ľ�ֵ��3.5��
imputer = KNNImputer(n_neighbors=2)
data2 = imputer.fit_transform(data)
print(data2)
