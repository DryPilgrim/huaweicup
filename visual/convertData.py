# coding: gbk

from turtle import title
import pandas as pd
import numpy as np
import os
from pprint import pprint
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

def process_batch_file(data_path="D:\\AYEAR1\\math_model\\2022\\solution\\dataB2"):
    """只需要更改csv_des和data_path"""
    csv_all=os.listdir(data_path)
    for csv in csv_all:        
        PLATE_ID=[]
        NODE_ID=[]
        X=[]
        Y=[]
        WIDTH=[]
        HEIGHT=[]
        TYPE=[]
        CUT=[]
        PARENT=[]
        print('---:',csv)
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")   
        # print("---:\n",data['PARENT'][399],data['PARENT'][400],data['PARENT'][401])     

        # plate_times:每个板使用的次数
        plate_times=list(data['PLATE_ID'].value_counts(sort=False))  
        flag=0 
        PLATE_ID.append(data['PLATE_ID'][0])
        NODE_ID.append(data['NODE_ID'][0])
        X.append(data['X'][0])
        Y.append(data['Y'][0])
        WIDTH.append(data['WIDTH'][0])
        HEIGHT.append(data['HEIGHT'][0])
        TYPE.append(data['TYPE'][0])
        CUT.append(data['CUT'][0])
        PARENT.append(data['PARENT'][0])
        for i in range(1,len(data['PLATE_ID'])):  
            if data['PLATE_ID'][i-1]==0 and data['PLATE_ID'][i]==0 and math.isnan(data['PARENT'][i]):
                # print("---data[400]:\n",data.iloc[400])
                PLATE_ID.append(PLATE_ID[-1]+1)
            elif data['PLATE_ID'][i]==PLATE_ID[-1]:
                # print("PLATE_ID[-1]:\n",PLATE_ID[-1])
                PLATE_ID.append(data['PLATE_ID'][i])           
            elif data['PLATE_ID'][i]>PLATE_ID[-1]:
                PLATE_ID.append(data['PLATE_ID'][i])         
            elif data['PLATE_ID'][i]<PLATE_ID[-1]:
                if data['PLATE_ID'][i]!=data['PLATE_ID'][i-1]:
                    PLATE_ID.append(PLATE_ID[-1]+1)
                elif data['PLATE_ID'][i]==data['PLATE_ID'][i-1]:
                    PLATE_ID.append(PLATE_ID[-1])
            else:          
                PLATE_ID.append('na')      
                # #统计0的个数
                # if flag < plate_times[int(data['PLATE_ID'][i])] and flag==0:
                #     PLATE_ID.append(PLATE_ID[-1]+1)
                #     flag+=1
                # elif flag < plate_times[int(data['PLATE_ID'][i])] and flag!=0:
                #     PLATE_ID.append(PLATE_ID[-1])
                # if flag+1 == plate_times[int(data['PLATE_ID'][i])]:
                #     flag=0
                # NODE_ID.append(NODE_ID[-1]+1)
            NODE_ID.append(data['NODE_ID'][i])
            X.append(data['X'][i])
            Y.append(data['Y'][i])
            WIDTH.append(data['WIDTH'][i])
            HEIGHT.append(data['HEIGHT'][i])
            TYPE.append(data['TYPE'][i])
            CUT.append(data['CUT'][i])
            PARENT.append(data['PARENT'][i])

        dic={
            "PLATE_ID":PLATE_ID,
            "NODE_ID":NODE_ID,
            "X":X,
            "Y":Y,
            "WIDTH":WIDTH,
            "HEIGHT":HEIGHT,
            "TYPE":TYPE,
            "CUT":CUT,
            "PARENT":PARENT
        }
        df=pd.DataFrame(dic)
        #存入csv
        csv_des="D:\\AYEAR1\\math_model\\2022\solution\\dataB2_solution"
        df.to_csv(csv_des+"\\"+csv.split(".")[0]+"_new.csv",index=False)


process_batch_file()
"""
只需要更改data_path和csv_des
"""

