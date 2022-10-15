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
# 数据载入到 DataFrame 对象
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

# 返回第一行和第二行
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

# print(df.iloc[-1:])#最后1行
# print(df.loc[-1:])#整个df

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
   # 把data_1_actual中小于0的数，
   data_1_actual[ data_1_actual< 0 ] = np.nan
   # print('---<0:\n',data_1_actual)

   for indexs in data_1_actual.columns:
      if indexs =='time':
         continue
      data_1_actual['rownum'] = np.arange(data_1_actual.shape[0])
      df_nona = data_1_actual.dropna(subset = [indexs])#当前位置元素为空，删除当前元素所在的行
      # print('---after dropna:\n',df_nona)
      f = interpolate.interp1d(df_nona['rownum'], df_nona[indexs],fill_value="extrapolate") #构建从 rownum 到 具体字段值 的函数映射
      data_1_actual[indexs] = f(data_1_actual['rownum']) #这一步没有效用吧
      # print('---after interpolate:\n',data_1_actual)

   data_1_actual = data_1_actual.drop(columns=['rownum'])
   return data_1_actual

print(df2['duration'])
df2_=interpolate1d(df2)
print(df2_)


"""interpolate.interp1d
用现有的数据来构建一个函数(f = interpolate.interp1d(x, y))，遇到新的输入时就可以用这个函数来计算出新的输出！

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