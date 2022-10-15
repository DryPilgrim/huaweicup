# coding: gbk

from turtle import title
import pandas as pd
import numpy as np
import os, copy
from pprint import pprint
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

def plot_colors_batch(data_path="D:\\FirstTaskImages\\BuffImages"):
    #<class 'pandas.core.frame.DataFrame'>
    csv_all=os.listdir(data_path)
    csv_all.remove(".DS_Store")
    data_des="D:\\FirstTaskImages\\BuffImages_new\\"
    k=0
    for csv in csv_all:
        csv_new=copy.deepcopy(csv)
        print(csv_new)
        index=int(csv_new.split("(")[-1].split(")")[0])
        os.rename(data_path+"\\"+csv_new,data_des+str(index)+".jpg")
        k+=1

       

plot_colors_batch()