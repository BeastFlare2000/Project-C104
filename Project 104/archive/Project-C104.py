import csv
import pandas as pd
import statistics

df = pd.read_csv('data.csv')

print(f"Mean of savings - {statistics.mean(df)}")
print(f"Median of savings - {statistics.median(df)}")
print(f"Mode of savings - {statistics.mode(df)}")