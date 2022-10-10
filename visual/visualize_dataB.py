# coding: gbk

from turtle import title
import pandas as pd
import numpy as np
import os
from pprint import pprint
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

def plot(x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"]),y = np.array([12, 22, 6, 18]),title='������������������',xlab='item_order',ylab="item_colors"):       
    plt.rcParams['font.sans-serif'] = ['SimHei']  # ָ��Ĭ������
    plt.rcParams['axes.unicode_minus'] = False  # �������ͼ���Ǹ���'-'��ʾΪ���������
    plt.title(title)  # ���ñ���
    plt.xlabel(xlab)  # ����x�����ǩ
    plt.xticks(rotation=30)
    plt.ylabel(ylab)  # ����y�����ǩ
    plt.plot(x,y,linestyle='dotted')
    plt.show()

def plot_color_item(data_path="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B\\dataB5.csv"):
    #<class 'pandas.core.frame.DataFrame'>
    data=pd.read_csv(data_path)
    x=[]#����
    y=[]#��ɫ

    # ��ȡ���ж�����
    order_list=data["item_order"]
    order_list=list(set(order_list))#ȥ��
    order_list.sort()
    # print(len(order_list), '\n',order_list)

    # ����item_order��������Ϊ���ɸ��ӱ�
    data_orders=data.groupby(data.item_order)

    for li in order_list:
        x.append(li)
        data_order=data_orders.get_group(li)
        # ����ÿ�������Ļ�ɫ��
        y.append(len(data_order["item_material"].value_counts()))
    print(x,'---\n',y)
    dic={
        "item_order":x,
        "item_colors":y
    }
    df=pd.DataFrame(dic)
    df=df.sort_values(by='item_colors',ascending=False)

    #����csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1].split(".")[0]+"_statistic.csv",index=False)
    #��ͼ
    # plot(np.array(df['item_order']),np.array(df['item_colors']), "����������ɫ������","item_order","item_colors")

def plot_area_item(data_path="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B\\dataB2.csv"):
    #<class 'pandas.core.frame.DataFrame'>
    data=pd.read_csv(data_path)
    x=[]#����
    y=[]#���

    # ��ȡ���ж�����
    order_list=data["item_order"]
    order_list=list(set(order_list))#ȥ��
    order_list.sort()
    # print(len(order_list), '\n',order_list)

    # ����item_order��������Ϊ���ɸ��ӱ�
    data_orders=data.groupby(data.item_order)

    for li in order_list:
        area=[]
        x.append(li)
        data_order=data_orders.get_group(li)
        # ����ÿ�������������
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

    #����csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1].split(".")[0]+"_area_statistic.csv",index=False)
    #��ͼ
    # title='��������չ���ܷ�'
    # ylab='item_areas'
    # plot(np.array(df['item_order']),np.array(df['item_area']),title,ylab)


def plot_n_item(data_path="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B\\dataB2.csv"):
    #<class 'pandas.core.frame.DataFrame'>
    data=pd.read_csv(data_path)
    x=[]#����
    y=[]#������������

    # ��ȡ���ж�����
    order_list=data["item_order"]
    order_list=list(set(order_list))#ȥ��
    order_list.sort()
    # print(len(order_list), '\n',order_list)

    # ����item_order��������Ϊ���ɸ��ӱ�
    data_orders=data.groupby(data.item_order)

    for li in order_list:
        area=[]
        x.append(li)
        data_order=data_orders.get_group(li)
        # ����ÿ�������Ĺ�����        
        y.append(len(data_order['item_order']))
    print(x,'---\n',y)
    dic={
        "item_order":x,
        "item_n":y
    }
    df=pd.DataFrame(dic)
    df=df.sort_values(by='item_n',ascending=False)

    #����csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1].split(".")[0]+"_n_statistic.csv",index=False)
    # #��ͼ
    # title='����������'
    # ylab='item_n'
    # plot(np.array(df['item_order']),np.array(df['item_n']),title,ylab)


def plot_colors_batch(data_path="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\batched_data\\batched-C_DataB2"):
    #<class 'pandas.core.frame.DataFrame'>
    csv_all=os.listdir(data_path)
    x=[]#����
    y=[]#��������������
    z=[]#�����Ӧԭʼ�����Ļ�ɫ��֮��
    pos=[]#λ��
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])
        pos.append(int(csv.split('.')[0].split("-")[-1]))

        # print('---:\n',len(data['����'].value_counts()),data['����'].value_counts())
        #value_counts ͳ�Ƹ��в�ֵͬ���ֵĴ�������len()����ȡ���ж����ֲ�ͬ��ֵ
        y.append(len(data['����'].value_counts()))

        # ��ȡ���ж�����
        order_list=data["�������"]
        order_list=list(set(order_list))#ȥ��
        order_list.sort()
        # print("len(order_list):\n",len(order_list), '\n',order_list)

        # ����item_order��������Ϊ���ɸ��ӱ�
        data_orders=data.groupby(data.�������)

        z_tmp=[]
        for li in order_list:
            # x.append(li)
            data_order=data_orders.get_group(li)
            # ����ÿ�������Ļ�ɫ��
            z_tmp.append(len(data_order["����"].value_counts()))
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
    #����csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\batched_data_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1]+"_colors_statistic.csv",index=False)
    
    #��ͼ
    # title='����������������������'
    # xlab='item_batch'
    # ylab='item_colors'
    # plot(np.array(df['item_batch']),np.array(df['item_colors']),title,xlab,ylab)

def plot_itemNum_batch(data_path="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\batched_data\\batched-C_DataB2"):
    #<class 'pandas.core.frame.DataFrame'>
    csv_all=os.listdir(data_path)
    x=[]#����
    y=[]#����������
    pos=[]#λ��
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])

        print('---:\n',data['����'].sum())
        #value_counts ͳ�Ƹ��в�ֵͬ���ֵĴ�������len()����ȡ���ж����ֲ�ͬ��ֵ
        y.append(data['����'].sum())
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
    #����csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\batched_data_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1]+"_itemNum_statistic.csv",index=False)

def plot_itemArea_batch(data_path="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\batched_data\\batched-C_DataB2"):
    #<class 'pandas.core.frame.DataFrame'>
    csv_all=os.listdir(data_path)
    x=[]#������
    y=[]#�������������
    pos=[]#λ��
    area=[]
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])
        pos.append(int(csv.split('.')[0].split("-")[-1]))

        # ����ÿ�������������
        for l,w in zip(data["��"],data['��']):
            # print('--:\n',data_order["item_length"])
            area.append(w*l//100000)
        area_all=sum(area)

        #value_counts ͳ�Ƹ��в�ֵͬ���ֵĴ�������len()����ȡ���ж����ֲ�ͬ��ֵ
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
    #����csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\batched_data_statistic"
    df.to_csv(csv_des+"\\"+data_path.split("\\")[-1]+"_itemArea_statistic.csv",index=False)


def get_colors_tabel(data_path="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B"):
    csv_all=os.listdir(data_path)
    x=[]#���ݼ�
    y=[]#����������
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv)#,encoding="gbk"
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])

        # print('---:\n',len(data['����'].value_counts()),data['����'].value_counts())
        y.append(len(data['item_material'].value_counts()))

        print('---database:\n',x,'\n---colors\n',y)
        dic={
            "database":x,
            "colors":y
        }
        df=pd.DataFrame(dic)
        df=df.sort_values(by='colors',ascending=False)
    #����csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B_statistic"
    df.to_csv(csv_des+"\\"+"DataB_colors_statistic.csv",index=False)
    #��ͼ
    # title='�����������ݼ�����������'
    # xlab='database'
    # ylab='colors'
    # plot(np.array(df['database']),np.array(df['colors']),title,xlab,ylab)

def get_orderNum_tabel(data_path="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B"):
    #<class 'pandas.core.frame.DataFrame'> 
    csv_all=os.listdir(data_path)
    x=[]#���id
    y=[]#��������
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])

        # ��ȡ���ж�����
        order_list=data["item_order"]
        order_list=list(set(order_list))
        order_list.sort()
        # print('---:\n',len(data['����'].value_counts()),data['����'].value_counts())
        y.append(len(order_list))

    print(x,'---\n',y)
    dic={
        "tabel":x,
        "order_num":y
    }
    df=pd.DataFrame(dic)
    df=df.sort_values(by='tabel')
    print('---df:\n',df)
    #����csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B_statistic"
    df.to_csv(csv_des+"\\"+"DataB_orderNum_statistic.csv",index=False)

def get_area_tabel(data_path="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B"):
    #<class 'pandas.core.frame.DataFrame'> 
    csv_all=os.listdir(data_path)
    x=[]#���id
    y=[]#�����
    for csv in csv_all:
        data=pd.read_csv(data_path+"\\"+csv,encoding="gbk")
        # print('---:\n',csv.split('.')[0])
        x.append(csv.split('.')[0])

        # ����ÿ�����������
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
    #����csv
    csv_des="D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B_statistic"
    df.to_csv(csv_des+"\\"+"DataB_area_statistic.csv",index=False)


# data=pd.read_csv("D:\\AYEAR1\\math_model\\2022\\2022���й��о�����ѧ��ģ��������\\������2-���ݼ�B\\dataB2.csv")#<class 'pandas.core.frame.DataFrame'>
# print(type(data),'\n',data.head())
# # ��ȡ���ж�����
# order_list=data["item_order"]
# order_list=list(set(order_list))
# order_list.sort()
# # print(len(order_list), '\n',order_list)
# x=order_list
# # ����item_order��������Ϊ���ɸ��ӱ�
# data_order=data.groupby(data.item_order)
# data_order1=data_order.get_group("order1")
# ����ÿ�������Ļ�ɫ��
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