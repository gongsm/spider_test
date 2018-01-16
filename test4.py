import pandas as pd
import json
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv" 
df = pd.read_csv(data_url)
df.to_csv('F:\\workspace\\pythontest\src\\spider\\demo.csv', encoding='utf-8', index=False) 
#print df.describe()
group = df.groupby('day') 