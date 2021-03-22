import pandas as pd
import numpy as np
import csv


i=0
j=0

for j in range(0, 60):
    for i in range(0, 60):
        data = pd.read_csv("C:/Users/mcnl/Desktop/C3.csv")
        df = pd.DataFrame(data)

        datai = df['Date first seen'] == "0:"+str(j).zfill(2)+":"+str(i).zfill(2)
        data_i = df[datai]

        data_u = data_i[data_i['class'].str.contains('unknown')]
        data_s = data_i[data_i['class'].str.contains('suspicious')]
        data_n = data_i[data_i['class'].str.contains('normal')]

        a = len(data_u)
        b = len(data_s)
        c = len(data_n)

        if (a >= b) and (a >= c):
            largest = a
        elif (b >= a) and (b >= c):
            largest = b
        else:
            largest = c

        if largest == a:
            data_i = data_u
            class1 = "unknown"

        if largest == b:
            data_i = data_s
            class1 = "suspicious"

        if largest == c:
            data_i = data_n
            class1 = "normal"

        dataq = df['Date first seen'] == "0:" + str(j).zfill(2) + ":" + str(i).zfill(2)
        data_q = df[dataq]

        data_a = data_i[data_i['Proto'].str.contains('TCP  ')]
        data_b = data_i[data_i['Proto'].str.contains('UDP  ')]
        data_c = data_i[data_i['Proto'].str.contains('ICMP ')]
        data_d = data_i[data_i['Proto'].str.contains('GRE  ')]

        a = len(data_a)
        b = len(data_b)
        c = len(data_c)
        d = len(data_d)

        if (a >= b) and (a >= c) and (a >= d):
            largest = a
        elif (b >= a) and (b >= c) and (b >= d):
            largest = b
        elif (c >= a) and (c >= b) and (c >= d):
            largest = c
        elif (d >= a) and (d >= b) and (d >= c):
            largest = d

        if largest == a:
            data_q = data_a
            class2 = 1

        if largest == b:
            data_q = data_b
            class2 = 2

        if largest == c:
            data_q = data_c
            class2 = 3

        if largest == d:
            data_q = data_d
            class2 = 4

        datap = df['Date first seen'] == "0:" + str(j).zfill(2) + ":" + str(i).zfill(2)
        data_p = df[datap]




        data_1 = data_i[data_i['Flags']=='....S.']
        data_2 = data_i[data_i['Flags']=='.A.R..']
        data_3 = data_i[data_i['Flags']=='.AP.SF']
        data_4 = data_i[data_i['Flags']=='.AP.S.']
        data_5 = data_i[data_i['Flags']=='.APRS.']
        data_6 = data_i[data_i['Flags']=='.APRSF']
        data_7 = data_i[data_i['Flags']=='...RS.']
        data_8 = data_i[data_i['Flags']=='.A..S.']
        data_9 = data_i[data_i['Flags']=='  0xdb']
        data_10 = data_i[data_i['Flags']=='......']
        data_11 = data_i[data_i['Flags']=='.A..SF']
        data_12 = data_i[data_i['Flags']=='.A.RS.']
        data_13 = data_i[data_i['Flags']=='.A.RSF']
        data_14 = data_i[data_i['Flags']=='.A....']
        data_15 = data_i[data_i['Flags']=='...R..']
        data_16 = data_i[data_i['Flags']=='  0xd7']
        data_17 = data_i[data_i['Flags']=='.AP…']
        data_18 = data_i[data_i['Flags']=='.A.R.F']
        data_19 = data_i[data_i['Flags']=='  0xc2']
        data_20 = data_i[data_i['Flags']=='  0xda']
        data_21 = data_i[data_i['Flags']=='.AP...']
        data_22 = data_i[data_i['Flags']=='  0xd2']
        data_23 = data_i[data_i['Flags']=='  0xdf']
        data_24 = data_i[data_i['Flags']=='  0x53']
        data_25 = data_i[data_i['Flags']=='  0xd3']
        data_26 = data_i[data_i['Flags']=='  0xd6']


        a1 = len(data_1)
        a2 = len(data_2)
        a3 = len(data_3)
        a4 = len(data_4)
        a5 = len(data_5)
        a6 = len(data_6)
        a7 = len(data_7)
        a8 = len(data_8)
        a9 = len(data_9)
        a10 = len(data_10)
        a11 = len(data_11)
        a12 = len(data_12)
        a13 = len(data_13)
        a14 = len(data_14)
        a15 = len(data_15)
        a16 = len(data_16)
        a17 = len(data_17)
        a18 = len(data_18)
        a19 = len(data_19)
        a20 = len(data_20)
        a21 = len(data_21)
        a22 = len(data_22)
        a23 = len(data_23)
        a24 = len(data_24)
        a25 = len(data_25)
        a26 = len(data_26)

        def max_value(max_list):
            n=len(max_list)
            maxValue=max_list[0]
            for i in range(1,n):
                if max_list[i]>maxValue:
                    maxValue = max_list[i]
            return maxValue

        max_list=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26]


        if max_value(max_list) == a1:
            data_p = data_1
            class3 = 1

        if max_value(max_list) == a2:
            data_p = data_2
            class3 = 2

        if max_value(max_list) == a3:
            data_p = data_3
            class3 = 3

        if max_value(max_list) == a4:
            data_p = data_4
            class3 = 4

        if max_value(max_list) == a5:
            data_p = data_5
            class3 = 5

        if max_value(max_list) == a6:
            data_p = data_6
            class3 = 6

        if max_value(max_list) == a7:
            data_p = data_7
            class3 = 7

        if max_value(max_list) == a8:
            data_p = data_8
            class3 = 8

        if max_value(max_list) == a9:
            data_p = data_9
            class3 = 9

        if max_value(max_list) == a10:
            data_p = data_10
            class3 = 10

        if max_value(max_list) == a11:
            data_p = data_11
            class3 = 11

        if max_value(max_list) == a12:
            data_p = data_12
            class3 = 12

        if max_value(max_list) == a13:
            data_p = data_13
            class3 = 13

        if max_value(max_list) == a14:
            data_p = data_14
            class3 = 14

        if max_value(max_list) == a15:
            data_p = data_15
            class3 = 15

        if max_value(max_list) == a16:
            data_p = data_16
            class3 = 16

        if max_value(max_list) == a17:
            data_p = data_17
            class3 = 17

        if max_value(max_list) == a18:
            data_p = data_18
            class3 = 18

        if max_value(max_list) == a19:
            data_p = data_19
            class3 = 19

        if max_value(max_list) == a20:
            data_p = data_20
            class3 = 20

        if max_value(max_list) == a21:
            data_p = data_21
            class3 = 21

        if max_value(max_list) == a22:
            data_p = data_22
            class3 = 22

        if max_value(max_list) == a23:
            data_p = data_23
            class3 = 23

        if max_value(max_list) == a24:
            data_p = data_24
            class3 = 24

        if max_value(max_list) == a25:
            data_p = data_25
            class3 = 25

        if max_value(max_list) == a26:
            data_p = data_26
            class3 = 26



        data_i_duration = data_i.iloc[:, [1]]
        data_i_duration_average = np.mean(data_i_duration)
        data_i_duration_std = np.std(data_i_duration,axis=0)
        data_i_duration_var = np.var(data_i_duration,axis=0)

        data_i_Src_Pt = data_i.iloc[:, [3]]
        data_i_Src_Pt_average = np.mean(data_i_Src_Pt)
        data_i_Src_Pt_std = np.std(data_i_Src_Pt)
        data_i_Src_Pt_var = np.var(data_i_Src_Pt)

        data_i_Dst_Pt = data_i.iloc[:, [4]]
        data_i_Dst_Pt_average = np.mean(data_i_Dst_Pt)
        data_i_Dst_Pt_std = np.std(data_i_Dst_Pt)
        data_i_Dst_Pt_var = np.var(data_i_Dst_Pt)

        data_i_Packets = data_i.iloc[:, [5]]
        data_i_Packets_average = np.mean(data_i_Packets)
        data_i_Packets_std = np.std(data_i_Packets)
        data_i_Packets_var = np.var(data_i_Packets)

        data_i_Bytes = data_i.iloc[:, [6]]
        data_i_Bytes_average = np.mean(data_i_Bytes)
        data_i_Bytes_std = np.std(data_i_Bytes)
        data_i_Bytes_var = np.var(data_i_Bytes)

        values=[[float(data_i_duration_average),float(data_i_duration_std.values),float(data_i_duration_var.values),float(data_i_Src_Pt_average),float(data_i_Src_Pt_std.values),float(data_i_Src_Pt_var.values),float(data_i_Dst_Pt_average),float(data_i_Dst_Pt_std.values),float(data_i_Dst_Pt_var.values),float(data_i_Packets_average),float(data_i_Packets_std.values),float(data_i_Packets_var.values),float(data_i_Bytes_average),float(data_i_Bytes_std.values),float(data_i_Bytes_var.values),class1,class2,class3]]

        index2="0:"+str(j).zfill(2)+":"+str(i).zfill(2)
        df1=pd.DataFrame(values,index=[index2])
        df1 = pd.DataFrame(df1)  # 데이터 프레임으로 전환
        df1.to_csv("C9.csv", mode='a')

        i=i+1
    j=j+1

#1시간 후
data = pd.read_csv("C:/Users/mcnl/Desktop/CIDDS.csv")
df = pd.DataFrame(data)
datai = df['Date first seen'] == "1:00:00"
data_i = df[datai]

data_u = data_i[data_i['class'].str.contains('unknown')]
data_s = data_i[data_i['class'].str.contains('suspicious')]
data_n = data_i[data_i['class'].str.contains('normal')]

a = len(data_u)
b = len(data_s)
c = len(data_n)

if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

if largest == a:
    data_i = data_u
    class1 = "unknown"

if largest == b:
    data_i = data_s
    class1 = "suspicious"

if largest == c:
    data_i = data_n
    class1 = "normal"

dataq = df['Date first seen'] == "0:" + str(j).zfill(2) + ":" + str(i).zfill(2)
data_q = df[dataq]

data_a = data_i[data_i['Proto'].str.contains('TCP')]
data_b = data_i[data_i['Proto'].str.contains('UDP')]
data_c = data_i[data_i['Proto'].str.contains('ICMP')]
data_d = data_i[data_i['Proto'].str.contains('GRE')]

a = len(data_a)
b = len(data_b)
c = len(data_c)
d = len(data_d)

if (a >= b) and (a >= c) and (a >= d):
    largest = a
elif (b >= a) and (b >= c) and (b >= d):
    largest = b
elif (c >= a) and (c >= b) and (c >= d):
    largest = c
elif (d >= a) and (d >= b) and (d >= c):
    largest = d

if largest == a:
    data_q = data_a
    class2 = 1

if largest == b:
    data_q = data_b
    class2 = 2

if largest == c:
    data_q = data_c
    class2 = 3

if largest == d:
    data_q = data_d
    class2 = 4

datap = df['Date first seen'] == "0:" + str(j).zfill(2) + ":" + str(i).zfill(2)
data_p = df[datap]

data_1 = data_i[data_i['Flags']=='....S.']
data_2 = data_i[data_i['Flags']=='.A.R..']
data_3 = data_i[data_i['Flags']=='.AP.SF']
data_4 = data_i[data_i['Flags']=='.AP.S.']
data_5 = data_i[data_i['Flags']=='.APRS.']
data_6 = data_i[data_i['Flags']=='.APRSF']
data_7 = data_i[data_i['Flags']=='...RS.']
data_8 = data_i[data_i['Flags']=='.A..S.']
data_9 = data_i[data_i['Flags']=='  0xdb']
data_10 = data_i[data_i['Flags']=='......']
data_11 = data_i[data_i['Flags']=='.A..SF']
data_12 = data_i[data_i['Flags']=='.A.RS.']
data_13 = data_i[data_i['Flags']=='.A.RSF']
data_14 = data_i[data_i['Flags']=='.A....']
data_15 = data_i[data_i['Flags']=='...R..']
data_16 = data_i[data_i['Flags']=='  0xd7']
data_17 = data_i[data_i['Flags']=='.AP…']
data_18 = data_i[data_i['Flags']=='.A.R.F']
data_19 = data_i[data_i['Flags']=='  0xc2']
data_20 = data_i[data_i['Flags']=='  0xda']
data_21 = data_i[data_i['Flags']=='.AP...']
data_22 = data_i[data_i['Flags']=='  0xd2']
data_23 = data_i[data_i['Flags']=='  0xdf']
data_24 = data_i[data_i['Flags']=='  0x53']
data_25 = data_i[data_i['Flags']=='  0xd3']
data_26 = data_i[data_i['Flags']=='  0xd6']


a1 = len(data_1)
a2 = len(data_2)
a3 = len(data_3)
a4 = len(data_4)
a5 = len(data_5)
a6 = len(data_6)
a7 = len(data_7)
a8 = len(data_8)
a9 = len(data_9)
a10 = len(data_10)
a11 = len(data_11)
a12 = len(data_12)
a13 = len(data_13)
a14 = len(data_14)
a15 = len(data_15)
a16 = len(data_16)
a17 = len(data_17)
a18 = len(data_18)
a19 = len(data_19)
a20 = len(data_20)
a21 = len(data_21)
a22 = len(data_22)
a23 = len(data_23)
a24 = len(data_24)
a25 = len(data_25)
a26 = len(data_26)

def max_value(max_list):
    n=len(max_list)
    maxValue=max_list[0]
    for i in range(1,n):
        if max_list[i]>maxValue:
            maxValue = max_list[i]
    return maxValue

max_list=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26]


if max_value(max_list) == a1:
    data_p = data_1
    class3 = 1

if max_value(max_list) == a2:
    data_p = data_2
    class3 = 2

if max_value(max_list) == a3:
    data_p = data_3
    class3 = 3

if max_value(max_list) == a4:
    data_p = data_4
    class3 = 4

if max_value(max_list) == a5:
    data_p = data_5
    class3 = 5

if max_value(max_list) == a6:
    data_p = data_6
    class3 = 6

if max_value(max_list) == a7:
    data_p = data_7
    class3 = 7

if max_value(max_list) == a8:
    data_p = data_8
    class3 = 8

if max_value(max_list) == a9:
    data_p = data_9
    class3 = 9

if max_value(max_list) == a10:
    data_p = data_10
    class3 = 10

if max_value(max_list) == a11:
    data_p = data_11
    class3 = 11

if max_value(max_list) == a12:
    data_p = data_12
    class3 = 12

if max_value(max_list) == a13:
    data_p = data_13
    class3 = 13

if max_value(max_list) == a14:
    data_p = data_14
    class3 = 14

if max_value(max_list) == a15:
    data_p = data_15
    class3 = 15

if max_value(max_list) == a16:
    data_p = data_16
    class3 = 16

if max_value(max_list) == a17:
    data_p = data_17
    class3 = 17

if max_value(max_list) == a18:
    data_p = data_18
    class3 = 18

if max_value(max_list) == a19:
    data_p = data_19
    class3 = 19

if max_value(max_list) == a20:
    data_p = data_20
    class3 = 20

if max_value(max_list) == a21:
    data_p = data_21
    class3 = 21

if max_value(max_list) == a22:
    data_p = data_22
    class3 = 22

if max_value(max_list) == a23:
    data_p = data_23
    class3 = 23

if max_value(max_list) == a24:
    data_p = data_24
    class3 = 24

if max_value(max_list) == a25:
    data_p = data_25
    class3 = 25

if max_value(max_list) == a26:
    data_p = data_26
    class3 = 26



data_i_duration = data_i.iloc[:, [1]]
data_i_duration_average = np.mean(data_i_duration)
data_i_duration_std = np.std(data_i_duration,axis=0)
data_i_duration_var = np.var(data_i_duration,axis=0)

data_i_Src_Pt = data_i.iloc[:, [3]]
data_i_Src_Pt_average = np.mean(data_i_Src_Pt)
data_i_Src_Pt_std = np.std(data_i_Src_Pt)
data_i_Src_Pt_var = np.var(data_i_Src_Pt)

data_i_Dst_Pt = data_i.iloc[:, [4]]
data_i_Dst_Pt_average = np.mean(data_i_Dst_Pt)
data_i_Dst_Pt_std = np.std(data_i_Dst_Pt)
data_i_Dst_Pt_var = np.var(data_i_Dst_Pt)

data_i_Packets = data_i.iloc[:, [5]]
data_i_Packets_average = np.mean(data_i_Packets)
data_i_Packets_std = np.std(data_i_Packets)
data_i_Packets_var = np.var(data_i_Packets)

data_i_Bytes = data_i.iloc[:, [6]]
data_i_Bytes_average = np.mean(data_i_Bytes)
data_i_Bytes_std = np.std(data_i_Bytes)
data_i_Bytes_var = np.var(data_i_Bytes)

values=[[float(data_i_duration_average),float(data_i_duration_std.values),float(data_i_duration_var.values),float(data_i_Src_Pt_average),float(data_i_Src_Pt_std.values),float(data_i_Src_Pt_var.values),float(data_i_Dst_Pt_average),float(data_i_Dst_Pt_std.values),float(data_i_Dst_Pt_var.values),float(data_i_Packets_average),float(data_i_Packets_std.values),float(data_i_Packets_var.values),float(data_i_Bytes_average),float(data_i_Bytes_std.values),float(data_i_Bytes_var.values),class1,class2,class3]]

index2="0:"+str(j).zfill(2)+":"+str(i).zfill(2)
df1=pd.DataFrame(values,index=[index2])
df1 = pd.DataFrame(df1)  # 데이터 프레임으로 전환
df1.to_csv("C9.csv", mode='a')
