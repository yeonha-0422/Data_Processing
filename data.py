import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/mcnl/PycharmProjects/pythonProject13/GOAD/data/MetaDescription.csv")
X=df.iloc[::2,1:16]
X=X.to_numpy()
Y=df.iloc[::2,16]
Y=np.where(Y.str.contains('normal'),1,0)
