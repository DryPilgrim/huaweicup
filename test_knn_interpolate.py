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

#因为第二个样本的第一列特征3和第三列特征7，与第一行样本的第一列特征2和第三列特征8的欧氏距离最近，所以缺失值按照第一个样本来填充，填充值为4
imputer = KNNImputer(n_neighbors=1)
data1 = imputer.fit_transform(data)
print(data1)

#那么n_neighbors=2呢？此时根据欧氏距离算出最近相邻的是第一行样本与第四行样本，此时的填充值就是这两个样本第二列特征4和3的均值：3.5。
imputer = KNNImputer(n_neighbors=2)
data2 = imputer.fit_transform(data)
print(data2)
