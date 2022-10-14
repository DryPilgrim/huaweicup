# coding: gbk

from turtle import title
import pandas as pd
import numpy as np
import os
from pprint import pprint
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

def plot_colors_batch(data_path="D:\\AYEAR1\\math_model\\2022\问题二\\solution5"):
    #<class 'pandas.core.frame.DataFrame'>
    csv_all=os.listdir(data_path)
    x=[]#订单
    y=[]#组批材料种类数
    z=[]#批组对应原始订单的花色数之和
    pos=[]#位置
    PLATE_ID=[]
    NODE_ID=[]
    X=[]
    Y=[]
    WIDTH=[]
    HEIGHT=[]
    TYPE=[]
    CUT=[]
    PARENT=[]
    # print('---:\n',csv_all)
    for csv in csv_all:
        print('---:',csv)
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print(data['X'][5])
        # break
        # print('---:\n',csv.split('.')[0])
        # x.append(csv.split('.')[0])
        # pos.append(int(csv.split('.')[0].split("-")[-1])) 

        # plate_times:每个板使用的次数
        plate_times=list(data['PLATE_ID'].value_counts(sort=False))  
        flag=0 
        for i in range(len(data['PLATE_ID'])):
            if int(csv.split('-')[-2])==0 and int(csv.split('-')[-3])==0:
                PLATE_ID.append(data['PLATE_ID'][i])
                NODE_ID.append(data['NODE_ID'][i])
            else:
                
                #统计0的个数
                if flag < plate_times[int(data['PLATE_ID'][i])] and flag==0:
                    PLATE_ID.append(PLATE_ID[-1]+1)
                    flag+=1
                elif flag < plate_times[int(data['PLATE_ID'][i])] and flag!=0:
                    PLATE_ID.append(PLATE_ID[-1])
                if flag+1 == plate_times[int(data['PLATE_ID'][i])]:
                    flag=0
                NODE_ID.append(NODE_ID[-1]+1)
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
    # df=df.sort_values(by='item_pos')
    # print('---df:\n',df)
    #存入csv
    csv_des="D:\\AYEAR1\\math_model\\2022\问题二"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1]+".csv",index=False)

def test():
    x=[1,2,3,4,5]
    y=[2,3,3,3,4] 
    dic={"x":x,"y":y}
    df=pd.DataFrame(dic)
    print(df)
    print(df['y'].value_counts(sort=False))


# plot_colors_batch()
# test()

def scrapy_svg():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    import pywinauto

    chrome_driver="D:\\APPS\\Anaconda\\anaconda3\\envs\\allOne\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver)
    wait=WebDriverWait(driver,10)
    driver.get('https://librallu.gitlab.io/packing-viz/')
    # driver.switch_to.frame("limitsvg")

    elem_xpath='//*[@id="app"]/div/header/div/div[3]/div[1]/div/div[1]/div[1]/div'
    element=wait.until(EC.element_to_be_clickable((By.XPATH, elem_xpath)))

    elem = driver.find_elements(By.XPATH,elem_xpath)
    print('---:\n',elem[0])
    elem[0].click()

    time.sleep(1)
    # 通过窗口打开
    app = pywinauto.Desktop()
    # 通过弹框名称进入控件中
    win = app['打开']
    # 输入上传图片的地址
    win['打开'].type_keys(r'D:\\AYEAR1\\math_model\\2022\\问题二\\solution1\\dataB1-0-0-solution.csv')
    #点击打开按钮
    win['Button'].click()

def main():
    # plot_colors_batch()
    # test()
    scrapy_svg()

main()