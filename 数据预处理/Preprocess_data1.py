#!/usr/bin/env python
# coding: utf-8

# # 处理附件1中的数据

# In[1]:


import pandas as pd
import numpy as np
import os
from pprint import pprint
from scipy import interpolate


# # 1 加载数据

# In[4]:



data_1_hour_predict_raw = pd.read_excel('../data/附件1 监测点A空气质量预报基础数据.xlsx',sheet_name='监测点A逐小时污染物浓度与气象一次预报数据')
data_1_hour_actual_raw = pd.read_excel('../data/附件1 监测点A空气质量预报基础数据.xlsx',sheet_name='监测点A逐小时污染物浓度与气象实测数据')
data_1_day_actual_raw = pd.read_excel('../data/附件1 监测点A空气质量预报基础数据.xlsx',sheet_name='监测点A逐日污染物浓度实测数据')


# In[5]:


print('---\n',data_1_hour_predict_raw.head())
print('---\n',data_1_hour_actual_raw.head())
print('---\n',data_1_day_actual_raw.head())


# In[6]:


df_1_predict = data_1_hour_actual_raw
df_1_actual = data_1_day_actual_raw
# 更改dataframe的行标签或列标签 https://vimsky.com/examples/usage/python-pandas.DataFrame.set_axis.html
df_1_predict.set_axis(['time', 'place', 'so2','no2','pm10', 'pm2.5', 'o3','co','temperature', 'humidity', 'pressure','wind','direction'], axis='columns', inplace=True)
df_1_actual.set_axis(['time', 'place', 'so2','no2','pm10', 'pm2.5', 'o3','co'], axis='columns', inplace=True)

modeltime_df_actual = df_1_actual['time']
modeltime_df_pre = df_1_predict['time']

df_1_actual = df_1_actual.drop(columns=['place','time'])
df_1_predict = df_1_predict.drop(columns=['place','time'])
df_1_predict = df_1_predict.replace('—', np.nan)
df_1_predict = df_1_predict.astype('float')
df_1_predict[ df_1_predict< 0 ] = np.nan
# 重新插入time列
df_1_actual.insert(0, 'time', modeltime_df_actual)
df_1_predict.insert(0, 'time', modeltime_df_pre)

# 线性插值的方法需要单独处理最后一行的数据
data_1_actual = df_1_actual[0:-3] #为什么舍弃最后两行？缺失太多？

data_1_predict = df_1_predict
data_1_predict.iloc[-1:]['pm10'] =22.0

data_1_actual_knn = df_1_actual[0:-3]
data_1_predict_knn =df_1_predict


# # 2 插值

# ## 2.1 线性插值

# In[ ]:



for indexs in data_1_actual.columns:
    if indexs =='time':
        continue
    data_1_actual['rownum'] = np.arange(data_1_actual.shape[0])
    df_nona = data_1_actual.dropna(subset = [indexs])#当前位置元素为空，删除当前元素所在的行
    f = interpolate.interp1d(df_nona['rownum'], df_nona[indexs]) #构建从 rownum 到 具体字段值 的函数映射
    data_1_actual[indexs] = f(data_1_actual['rownum'])

data_1_actual = data_1_actual.drop(columns=['rownum'])

for indexs in data_1_predict.columns:
    if indexs =='time':
        continue
    data_1_predict['rownum'] = np.arange(data_1_predict.shape[0])
    df_nona = data_1_predict.dropna(subset = [indexs])
    f = interpolate.interp1d(df_nona['rownum'], df_nona[indexs])
    data_1_predict[indexs] = f(data_1_predict['rownum'])
data_1_predict = data_1_predict.drop(columns=['rownum'])


# In[ ]:


writer=pd.ExcelWriter('data/data_1_linear.xlsx')   #定义writer
data_1_hour_predict_raw.to_excel(writer,'监测点A逐小时污染物浓度与气象一次预报数据',index=False) 
data_1_predict.to_excel(writer,'监测点A逐小时污染物浓度与气象实测数据',index=False) # writer---writer；sheet名称---原始表（35698）
data_1_actual.to_excel(writer,'监测点A逐日污染物浓度实测数据',index=False)

writer.save()


# In[ ]:


data_1_predict


# ## 2.2 KNN插值

# In[ ]:



def knn_mean(ts, n):
    out = np.copy(ts)
    for i, val in enumerate(ts):
        if np.isnan(val):
            n_by_2 = np.ceil(n/2)
            lower = np.max([0, int(i-n_by_2)])
            upper = np.min([len(ts)+1, int(i+n_by_2)])
            ts_near = np.concatenate([ts[lower:i], ts[i:upper]])
            out[i] = np.nanmean(ts_near)
    return out
for indexs in data_1_actual_knn.columns:
    if indexs =='time':
        continue
    data_1_actual_knn[indexs] = knn_mean(data_1_actual_knn[indexs].values,8)
for indexs in data_1_predict_knn.columns:
    if indexs =='time':
        continue
    data_1_predict_knn[indexs] = knn_mean(data_1_predict_knn[indexs].values,8)


# In[ ]:


writer=pd.ExcelWriter('data/data_1_knn.xlsx')   #定义writer

data_1_hour_predict_raw.to_excel(writer,'监测点A逐小时污染物浓度与气象一次预报数据',index=False) 
data_1_predict_knn.to_excel(writer,'监测点A逐小时污染物浓度与气象实测数据',index=False) # writer---writer；sheet名称---原始表（35698）
data_1_actual_knn.to_excel(writer,'监测点A逐日污染物浓度实测数据',index=False)

writer.save()


# In[ ]:


data_1_predict_knn

