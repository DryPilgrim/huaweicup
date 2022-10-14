# coding: gbk

from turtle import title
import pandas as pd
import numpy as np
import os
from pprint import pprint
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

def scrapy_svg(csv_file):
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
    # csv_path=r'D:\AYEAR1\math_model\2022\问题二\solution1\dataB1-0-1-solution.csv'
    win['Edit'].type_keys(csv_file)
    #点击打开按钮
    win['打开'].click()
    time.sleep(1)

    #获取上传文件过后的网页源代码
    # limitsvg=driver.find_element_by_class_name('limitsvg svg')
    limitsvg=driver.find_element(By.CLASS_NAME,'limitsvg svg')
    source_code=limitsvg.get_attribute("outerHTML")
    with open("D:\\AYEAR1\\math_model\\2022\\solution\\"+csv_file.split("\\")[-2].split("_")[0]+"_svg"+"\\"+csv_file.split("_")[-2].split("\\")[-1]+"_svg.svg","w") as f:
        f.write(source_code)
    driver.close()
    # svg_xpath='//*[@id="app"]/div/main/div/div/div/div/div[1]/svg'
    # svg_elem = driver.find_elements(By.XPATH,svg_xpath)
    # print("driver.page_source:\n",driver.page_source)

    # with open('test.txt','w') as f:
    #     f.write(str(svg_elem))
    # for svg_txt in svg_elem:
    #     # svg_txt=svg_elem[0]
    #     print("---111:\n",svg_txt.text)
def change_name(data_path):
    csv_all=os.listdir(data_path)
    for csv in csv_all:     
        pass
def scapy_all(data_path):
    csv_all=os.listdir(data_path)
    for csv in csv_all:     
        scrapy_svg(r''+data_path+csv)

def main():
    # scrapy_svg(r'D:\AYEAR1\math_model\2022\solution\dataB1_solution\dataB1-0_new.csv')
    scapy_all("D:\\AYEAR1\\math_model\\2022\\solution\\dataB3_solution\\")

main()