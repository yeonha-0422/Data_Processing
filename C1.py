
import pandas as pd
import numpy as np

df=pd.read_csv("C:/Users/mcnl/Desktop/C1.csv")

df=df.sort_values(by=['Date first seen'], axis=0)
df
df.to_csv('C2.csv')