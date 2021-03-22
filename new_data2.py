import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/mcnl/Desktop/CIDDSCI.csv")
df=df.iloc[15547:172840,:]
df.to_csv('CIDDS19.csv')

