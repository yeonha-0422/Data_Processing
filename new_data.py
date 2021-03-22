

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/mcnl/Desktop/CIDDS.csv")
df['class'] = np.where(df['class']=='normal', 1, 0)
df.to_csv('CIDDS22.csv')

df = pd.read_csv("C:/Users/mcnl/Desktop/MetaDescription8.csv")
df['label'] = np.where(df['label']=='normal', 1, 0)
df.to_csv('MetaDescription88.csv')


df = pd.read_csv("C:/Users/mcnl/Desktop/MetaDescription32.csv")
df=df.astype(int)
df.to_csv('Meta2.csv')