import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/mcnl/Desktop/C3.csv")
df['class'] = np.where(df['class']=='normal', 1, 0)


df.loc[(df.Proto == 'TCP  '),'Proto']=1
df.loc[(df.Proto == 'UDP  '),'Proto']=2
df.loc[(df.Proto == 'ICMP '),'Proto']=3
df.loc[(df.Proto == 'GRE  '),'Proto']=4

df.loc[(df.Flags == '....S.'),'Flags']=1
df.loc[(df.Flags == '.A.R..'),'Flags']=2
df.loc[(df.Flags == '.AP.SF'),'Flags']=3
df.loc[(df.Flags == '.AP.S.'),'Flags']=4
df.loc[(df.Flags == '.APRS.'),'Flags']=5
df.loc[(df.Flags == '.APRSF'),'Flags']=6
df.loc[(df.Flags == '...RS.'),'Flags']=7
df.loc[(df.Flags == '.A..S.'),'Flags']=8
df.loc[(df.Flags == '  0xdb'),'Flags']=9
df.loc[(df.Flags == '......'),'Flags']=10
df.loc[(df.Flags == '.A..SF'),'Flags']=11
df.loc[(df.Flags == '.A.RS.'),'Flags']=12
df.loc[(df.Flags == '.A.RSF'),'Flags']=13
df.loc[(df.Flags == '.A....'),'Flags']=14
df.loc[(df.Flags == '...R..'),'Flags']=15
df.loc[(df.Flags == '  0xd7'),'Flags']=16
df.loc[(df.Flags == '.AP…'),'Flags']=17
df.loc[(df.Flags == '.A.R.F'),'Flags']=18
df.loc[(df.Flags == '  0xc2'),'Flags']=19
df.loc[(df.Flags == '  0xda'),'Flags']=20
df.loc[(df.Flags == '.AP...'),'Flags']=21
df.loc[(df.Flags == '  0xd2'),'Flags']=22
df.loc[(df.Flags == '  0xdf'),'Flags']=23
df.loc[(df.Flags == '  0x53'),'Flags']=24
df.loc[(df.Flags == '  0xd3'),'Flags']=25
df.loc[(df.Flags == '  0xd6'),'Flags']=26

df.to_csv('C5.csv')
