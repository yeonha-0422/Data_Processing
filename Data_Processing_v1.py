import pandas as pd
import numpy as np
import csv


i=0
j=0

for j in range(0, 60):
    for i in range(0, 60):
        data = pd.read_csv("C:/Users/mcnl/Desktop/CIDDS.csv")
        df = pd.DataFrame(data)

        datai = df['Date first seen'] == "0:"+str(j).zfill(2)+":"+str(i).zfill(2)
        data_i = df[datai]

        data_u=data_i[data_i['class'].str.contains('unknown')]
        data_s=data_i[data_i['class'].str.contains('suspicious')]
        data_n=data_i[data_i['class'].str.contains('normal')]

        a=len(data_u)
        b=len(data_s)
        c=len(data_n)

        if (a >= b) and (a >= c):
            largest = a
        elif (b >= a) and (b >= c):
            largest = b
        else:
            largest = c

        if largest==a:
            data_i=data_u
            class1="unknown"

        if largest==b:
            data_i=data_s
            class1="suspicious"

        if largest==c:
            data_i=data_n
            class1="normal"


        data_i_duration = data_i.iloc[:, [1]]
        data_i_duration_average = np.average(data_i_duration)
        data_i_duration_std = np.std(data_i_duration,axis=0)
        data_i_duration_var = np.var(data_i_duration,axis=0)

        data_i_Src_Pt = data_i.iloc[:, [2]]
        data_i_Src_Pt_average = np.average(data_i_Src_Pt)
        data_i_Src_Pt_std = np.std(data_i_Src_Pt)
        data_i_Src_Pt_var = np.var(data_i_Src_Pt)

        data_i_Dst_Pt = data_i.iloc[:, [3]]
        data_i_Dst_Pt_average = np.average(data_i_Dst_Pt)
        data_i_Dst_Pt_std = np.std(data_i_Dst_Pt)
        data_i_Dst_Pt_var = np.var(data_i_Dst_Pt)

        data_i_Packets = data_i.iloc[:, [4]]
        data_i_Packets_average = np.average(data_i_Packets)
        data_i_Packets_std = np.std(data_i_Packets)
        data_i_Packets_var = np.var(data_i_Packets)

        data_i_Bytes = data_i.iloc[:, [5]]
        data_i_Bytes_average = np.average(data_i_Bytes)
        data_i_Bytes_std = np.std(data_i_Bytes)
        data_i_Bytes_var = np.var(data_i_Bytes)

        values=[[float(data_i_duration_average),float(data_i_duration_std.values),float(data_i_duration_var.values),float(data_i_Src_Pt_average),float(data_i_Src_Pt_std.values),float(data_i_Src_Pt_var.values),float(data_i_Dst_Pt_average),float(data_i_Dst_Pt_std.values),float(data_i_Dst_Pt_var.values),float(data_i_Packets_average),float(data_i_Packets_std.values),float(data_i_Packets_var.values),float(data_i_Bytes_average),float(data_i_Bytes_std.values),float(data_i_Bytes_var.values),class1]]

        index2="0:"+str(j).zfill(2)+":"+str(i).zfill(2)
        df1=pd.DataFrame(values,index=[index2])
        df1 = pd.DataFrame(df1)  # 데이터 프레임으로 전환
        df1.to_csv("OutputResult11.csv", mode='a')

        i=i+1
    j=j+1

#1시간 후
data = pd.read_csv("C:/Users/mcnl/Desktop/CIDDS.csv")
df = pd.DataFrame(data)
datai = df['Date first seen'] == "1:00:00"
data_i = df[datai]

data_u=data_i[data_i['class'].str.contains('unknown')]
data_s=data_i[data_i['class'].str.contains('suspicious')]
data_n=data_i[data_i['class'].str.contains('normal')]

a=len(data_u)
b=len(data_s)
c=len(data_n)

if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

if largest==a:
    data_i=data_u
    class1 = "unknown"
if largest==b:
    data_i=data_s
    class1 = "suspicious"
if largest==c:
    data_i=data_n
    class1 = "normal"

data_i_duration = data_i.iloc[:, [1]]
data_i_duration_average = np.average(data_i_duration)
data_i_duration_std = np.std(data_i_duration,axis=0)
data_i_duration_var = np.var(data_i_duration,axis=0)

data_i_Src_Pt = data_i.iloc[:, [2]]
data_i_Src_Pt_average = np.average(data_i_Src_Pt)
data_i_Src_Pt_std = np.std(data_i_Src_Pt)
data_i_Src_Pt_var = np.var(data_i_Src_Pt)

data_i_Dst_Pt = data_i.iloc[:, [3]]
data_i_Dst_Pt_average = np.average(data_i_Dst_Pt)
data_i_Dst_Pt_std = np.std(data_i_Dst_Pt)
data_i_Dst_Pt_var = np.var(data_i_Dst_Pt)

data_i_Packets = data_i.iloc[:, [4]]
data_i_Packets_average = np.average(data_i_Packets)
data_i_Packets_std = np.std(data_i_Packets)
data_i_Packets_var = np.var(data_i_Packets)

data_i_Bytes = data_i.iloc[:, [5]]
data_i_Bytes_average = np.average(data_i_Bytes)
data_i_Bytes_std = np.std(data_i_Bytes)
data_i_Bytes_var = np.var(data_i_Bytes)

values= values=[[float(data_i_duration_average),float(data_i_duration_std.values),float(data_i_duration_var.values),float(data_i_Src_Pt_average),float(data_i_Src_Pt_std.values),float(data_i_Src_Pt_var.values),float(data_i_Dst_Pt_average),float(data_i_Dst_Pt_std.values),float(data_i_Dst_Pt_var.values),float(data_i_Packets_average),float(data_i_Packets_std.values),float(data_i_Packets_var.values),float(data_i_Bytes_average),float(data_i_Bytes_std.values),float(data_i_Bytes_var.values),class1]]
index2="1:00:00"
df1=pd.DataFrame(values,index=[index2])
df1 = pd.DataFrame(df1)  # 데이터 프레임으로 전환
df1.to_csv("OutputResult11.csv", mode='a')