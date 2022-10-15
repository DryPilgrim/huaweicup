# coding:gbk
from ftplib import parse229
import pandas as pd
import numpy as np
from scipy import interpolate
import copy

data = {
  "calories": [420, 380, -390],
  "duration": [50, -40, 45]
}
data2 = {
  "calories1": [-420, 380, 390,412,423,400],
  "calories2": [421, -381, 391,413,421,401],
  "calories3": [422, 382, -392,414,422,402],
  "duration": [50, -40, 45,51,46,55]
}
# �������뵽 DataFrame ����
df = pd.DataFrame(data)
# print(df[['calories1','calories2']])#error
df2 = pd.DataFrame(data2)
# print('-----:\n',df2.loc[df2[df2== -381,:]].index)
# print('-----:\n',df2[df2.duration == 45].index.to_list()[0])
# print(df)
"""
   calories  duration
0       420        50
1       380       -40
2      -390        45
"""

# ���ص�һ�к͵ڶ���
# print(df.loc[[0, 1]])

df_ = copy.deepcopy(df) 
df_[df_<0]=np.nan
print(df)
print(df_)
"""
   calories  duration
0     420.0      50.0
1     380.0       NaN
2       NaN      45.0
"""

# print(df.iloc[-1:])#���1��
# print(df.loc[-1:])#����df

# print(df_.shape) # (3,2)
df_['rownum']=np.arange(df_.shape[0])
df_nona=df_.dropna(subset=['calories'])
# print(df_nona)
"""
   calories  duration  rownum
0     420.0      50.0       0
1     380.0       NaN       1
"""

import matplotlib.pyplot as plt
f=interpolate.interp1d(df_nona['rownum'], df_nona['calories'])
df_nona['calories']=f(df_nona['rownum'])
# print(df_nona)

def interpolate1d(data_1_actual):   
   data_1_actual = data_1_actual.astype('float')
   # ��data_1_actual��С��0������
   data_1_actual[ data_1_actual< 0 ] = np.nan
   # print('---<0:\n',data_1_actual)

   for indexs in data_1_actual.columns:
      if indexs =='time':
         continue
      data_1_actual['rownum'] = np.arange(data_1_actual.shape[0])
      df_nona = data_1_actual.dropna(subset = [indexs])#��ǰλ��Ԫ��Ϊ�գ�ɾ����ǰԪ�����ڵ���
      # print('---after dropna:\n',df_nona)
      f = interpolate.interp1d(df_nona['rownum'], df_nona[indexs],fill_value="extrapolate") #������ rownum �� �����ֶ�ֵ �ĺ���ӳ��
      data_1_actual[indexs] = f(data_1_actual['rownum']) #��һ��û��Ч�ð�
      # print('---after interpolate:\n',data_1_actual)

   data_1_actual = data_1_actual.drop(columns=['rownum'])
   return data_1_actual

print(df2['duration'])
df2_=interpolate1d(df2)
print(df2_)


"""interpolate.interp1d
�����е�����������һ������(f = interpolate.interp1d(x, y))�������µ�����ʱ�Ϳ��������������������µ������

import matplotlib.pyplot as plt
from scipy import interpolate
x = np.arange(0, 10)
y = np.exp(-x/3.0)
f = interpolate.interp1d(x, y)

xnew = np.arange(0, 9, 0.1)
ynew = f(xnew)   # use interpolation function returned by `interp1d`
plt.plot(x, y, 'o', xnew, ynew, '*')
plt.show()
"""

x=[1.5,2,3]
y=[10,20,30]
dic={
   "l":x,
   "w":y
}
df=pd.DataFrame(dic)
for l,w in zip(df['l'],df['w']):
   print("---:\n",l*w)