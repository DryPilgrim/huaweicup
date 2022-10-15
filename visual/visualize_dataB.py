# coding: gbk

from turtle import title
import pandas as pd
import numpy as np
import os
from pprint import pprint
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

def plot(x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"]),y = np.array([12, 22, 6, 18]),title='工件订单材料种类数',xlab='item_order',ylab="item_colors"):       
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    plt.title(title)  # 设置标题
    plt.xlabel(xlab)  # 设置x坐标标签
    plt.xticks(rotation=30)
    plt.ylabel(ylab)  # 设置y坐标标签
    plt.plot(x,y,linestyle='dotted')
    plt.show()

def plot_color_item(data_path="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B\\dataB5.csv"):
    #<class 'pandas.core.frame.DataFrame'>
    data=pd.read_csv(data_path)
    x=[]#订单
    y=[]#花色

    # 获取所有订单号
    order_list=data["item_order"]
    order_list=list(set(order_list))#去重
    order_list.sort()
    # print(len(order_list), '\n',order_list)

    # 根据item_order，将大表分为若干个子表
    data_orders=data.groupby(data.item_order)

    for li in order_list:
        x.append(li)
        data_order=data_orders.get_group(li)
        # 计算每个订单的花色数
        y.append(len(data_order["item_material"].value_counts()))
    print(x,'---\n',y)
    dic={
        "item_order":x,
        "item_colors":y
    }
    df=pd.DataFrame(dic)
    df=df.sort_values(by='item_colors',ascending=False)

    #存入csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1].split(".")[0]+"_statistic.csv",index=False)
    #绘图
    # plot(np.array(df['item_order']),np.array(df['item_colors']), "工件订单颜色种类数","item_order","item_colors")

def plot_area_item(data_path="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B\\dataB2.csv"):
    #<class 'pandas.core.frame.DataFrame'>
    data=pd.read_csv(data_path)
    x=[]#订单
    y=[]#面积

    # 获取所有订单号
    order_list=data["item_order"]
    order_list=list(set(order_list))#去重
    order_list.sort()
    # print(len(order_list), '\n',order_list)

    # 根据item_order，将大表分为若干个子表
    data_orders=data.groupby(data.item_order)

    for li in order_list:
        area=[]
        x.append(li)
        data_order=data_orders.get_group(li)
        # 计算每个订单的面积和
        for l,w in zip(data_order["item_length"],data_order['item_width']):
            # print('--:\n',data_order["item_length"])
            area.append(w*l)
        area_all=sum(area)
        y.append(area_all)
    print(x,'---\n',y)
    dic={
        "item_order":x,
        "item_area":y
    }
    df=pd.DataFrame(dic)
    df=df.sort_values(by='item_area',ascending=False)

    #存入csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1].split(".")[0]+"_area_statistic.csv",index=False)
    #绘图
    # title='工件订单展开总方'
    # ylab='item_areas'
    # plot(np.array(df['item_order']),np.array(df['item_area']),title,ylab)


def plot_n_item(data_path="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B\\dataB2.csv"):
    #<class 'pandas.core.frame.DataFrame'>
    data=pd.read_csv(data_path)
    x=[]#订单
    y=[]#订单工件数量

    # 获取所有订单号
    order_list=data["item_order"]
    order_list=list(set(order_list))#去重
    order_list.sort()
    # print(len(order_list), '\n',order_list)

    # 根据item_order，将大表分为若干个子表
    data_orders=data.groupby(data.item_order)

    for li in order_list:
        area=[]
        x.append(li)
        data_order=data_orders.get_group(li)
        # 计算每个订单的工件数        
        y.append(len(data_order['item_order']))
    print(x,'---\n',y)
    dic={
        "item_order":x,
        "item_n":y
    }
    df=pd.DataFrame(dic)
    df=df.sort_values(by='item_n',ascending=False)

    #存入csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1].split(".")[0]+"_n_statistic.csv",index=False)
    # #绘图
    # title='工件订单数'
    # ylab='item_n'
    # plot(np.array(df['item_order']),np.array(df['item_n']),title,ylab)


def plot_colors_batch(data_path="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\batched_data\\batched-C_DataB2"):
    #<class 'pandas.core.frame.DataFrame'>
    csv_all=os.listdir(data_path)
    x=[]#订单
    y=[]#组批材料种类数
    z=[]#批组对应原始订单的花色数之和
    pos=[]#位置
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])
        pos.append(int(csv.split('.')[0].split("-")[-1]))

        # print('---:\n',len(data['材料'].value_counts()),data['材料'].value_counts())
        #value_counts 统计该列不同值出现的次数，用len()即可取出有多少种不同的值
        y.append(len(data['材料'].value_counts()))

        # 获取所有订单号
        order_list=data["订单编号"]
        order_list=list(set(order_list))#去重
        order_list.sort()
        # print("len(order_list):\n",len(order_list), '\n',order_list)

        # 根据item_order，将大表分为若干个子表
        data_orders=data.groupby(data.订单编号)

        z_tmp=[]
        for li in order_list:
            # x.append(li)
            data_order=data_orders.get_group(li)
            # 计算每个订单的花色数
            z_tmp.append(len(data_order["材料"].value_counts()))
        z.append(sum(z_tmp)) 

    # print(x,'---\n',y)
    dic={
        "item_batch":x,
        "item_color_batch":y,
        "item_colors_orders":z,
        "item_pos":pos
    }
    df=pd.DataFrame(dic)
    df=df.sort_values(by='item_pos')
    # print('---df:\n',df)
    #存入csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\batched_data_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1]+"_colors_statistic.csv",index=False)
    
    #绘图
    # title='工件订单组批材料种类数'
    # xlab='item_batch'
    # ylab='item_colors'
    # plot(np.array(df['item_batch']),np.array(df['item_colors']),title,xlab,ylab)

def plot_itemNum_batch(data_path="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\batched_data\\batched-C_DataB2"):
    #<class 'pandas.core.frame.DataFrame'>
    csv_all=os.listdir(data_path)
    x=[]#订单
    y=[]#组批工件数
    pos=[]#位置
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])

        print('---:\n',data['数量'].sum())
        #value_counts 统计该列不同值出现的次数，用len()即可取出有多少种不同的值
        y.append(data['数量'].sum())
        pos.append(int(csv.split('.')[0].split("-")[-1]))

    print(x,'---\n',y)
    dic={
        "item_batch":x,
        "item_num":y,
        "item_pos":pos
    }
    df=pd.DataFrame(dic)
    df=df.sort_values(by='item_pos')
    print('---df:\n',df)
    #存入csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\batched_data_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1]+"_itemNum_statistic.csv",index=False)

def plot_itemArea_batch(data_path="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\batched_data\\batched-C_DataB2"):
    #<class 'pandas.core.frame.DataFrame'>
    csv_all=os.listdir(data_path)
    x=[]#组批号
    y=[]#组批工件面积和
    pos=[]#位置
    area=[]
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])
        pos.append(int(csv.split('.')[0].split("-")[-1]))

        # 计算每个订单的面积和
        for l,w in zip(data["长"],data['宽']):
            # print('--:\n',data_order["item_length"])
            area.append(w*l//100000)
        area_all=sum(area)

        #value_counts 统计该列不同值出现的次数，用len()即可取出有多少种不同的值
        y.append(area_all)

        print(x,'---\n',y)
        dic={
            "item_batch":x,
            "item_area":y,
            "item_pos":pos
        }
        df=pd.DataFrame(dic)
        df=df.sort_values(by='item_pos')
    print('---df:\n',df)
    #存入csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\batched_data_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1]+"_itemArea_statistic.csv",index=False)


def get_colors_tabel(data_path="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B"):
    csv_all=os.listdir(data_path)
    x=[]#数据集
    y=[]#材料种类数
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv)#,encoding="gbk"
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])

        # print('---:\n',len(data['材料'].value_counts()),data['材料'].value_counts())
        y.append(len(data['item_material'].value_counts()))

        print('---database:\n',x,'\n---colors\n',y)
        dic={
            "database":x,
            "colors":y
        }
        df=pd.DataFrame(dic)
        df=df.sort_values(by='colors',ascending=False)
    #存入csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B_statistic"
    df.to_csv(csv_des+"\\"+"DataB_colors_statistic.csv",index=False)
    #绘图
    # title='工件订单数据集材料种类数'
    # xlab='database'
    # ylab='colors'
    # plot(np.array(df['database']),np.array(df['colors']),title,xlab,ylab)

def get_orderNum_tabel(data_path="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B"):
    #<class 'pandas.core.frame.DataFrame'> 
    csv_all=os.listdir(data_path)
    x=[]#表格id
    y=[]#订单总数
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])

        # 获取所有订单号
        order_list=data["item_order"]
        order_list=list(set(order_list))
        order_list.sort()
        # print('---:\n',len(data['材料'].value_counts()),data['材料'].value_counts())
        y.append(len(order_list))

    print(x,'---\n',y)
    dic={
        "tabel":x,
        "order_num":y
    }
    df=pd.DataFrame(dic)
    df=df.sort_values(by='tabel')
    print('---df:\n',df)
    #存入csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B_statistic"
    df.to_csv(csv_des+"\\"+"DataB_orderNum_statistic.csv",index=False)

def get_area_tabel(data_path="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B"):
    #<class 'pandas.core.frame.DataFrame'> 
    csv_all=os.listdir(data_path)
    x=[]#表格id
    y=[]#总面积
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])

        # 计算每个表格的面积和
        area=[]
        for l,w in zip(data["item_length"],data['item_width']):
            # print('--:\n',data["item_length"])
            area.append(int(w*l/100000))
        area_all=sum(area)
        y.append(area_all)

    print(x,'---\n',y)
    dic={
        "tabel":x,
        "area":y
    }
    df=pd.DataFrame(dic)
    df=df.sort_values(by='tabel')
    print('---df:\n',df)
    #存入csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B_statistic"
    df.to_csv(csv_des+"\\"+"DataB_area_statistic.csv",index=False)


# data=pd.read_csv("D:\\AYEAR1\\math_model\\2022\\2022年中国研究生数学建模竞赛试题\\子问题2-数据集B\\dataB2.csv")#<class 'pandas.core.frame.DataFrame'>
# print(type(data),'\n',data.head())
# # 获取所有订单号
# order_list=data["item_order"]
# order_list=list(set(order_list))
# order_list.sort()
# # print(len(order_list), '\n',order_list)
# x=order_list
# # 根据item_order，将大表分为若干个子表
# data_order=data.groupby(data.item_order)
# data_order1=data_order.get_group("order1")
# 计算每个订单的花色数
# print(data_order1["item_material"].value_counts())

def main():
    # plot_color_item()
    # plot_area_item()
    # plot_n_item()
    plot_colors_batch()
    # plot_itemNum_batch()
    # plot_itemArea_batch()
    # get_colors_tabel()
    # get_orderNum_tabel()
    # get_area_tabel()

main()