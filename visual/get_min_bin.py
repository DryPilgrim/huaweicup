import json, os
import pandas as pd


def get_bin(json_dir='jsons/'):
    import json
    
    jsons=os.listdir(json_dir)
    file_list=[]
    FullWastePercentage_list=[]
    NumberOfBins_list=[]
    Time_list=[]

    for json_i in jsons:
        json_file=open(json_dir+json_i)
        dic=json.load(json_file)

        FullWastePercentage=dic.get(list(dic.keys())[-1])['FullWastePercentage']
        NumberOfBins=dic.get(list(dic.keys())[-1])['NumberOfBins']
        Time=dic.get(list(dic.keys())[-1])['Time']

        print(FullWastePercentage,NumberOfBins)

        file_list.append(json_i)
        FullWastePercentage_list.append(FullWastePercentage)
        NumberOfBins_list.append(NumberOfBins)
        Time_list.append(Time)
        df=pd.DataFrame({'file_name':file_list,'FullWastePercentage':FullWastePercentage_list,'NumberOfBins':NumberOfBins_list,"Time":Time_list})
        #columns=['file_name','FullWastePercentage','NumberOfBins']
        df.to_csv("bins_out.csv")

get_bin('jsons/')