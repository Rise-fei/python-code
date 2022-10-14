import pandas as pd


df = pd.read_csv("a.csv", header=0)
df = df.dropna(axis=0, how="all")
df = df.fillna("")
values_list = df.values.tolist()