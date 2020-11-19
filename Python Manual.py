import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from pathlib import Path

data = pd.read_csv('FH.csv', usecols = ['Well ID', 'Manual Computed Water Level (masl)', 'Date'])
print(data.head())
print(data)


dataframe1 = data[data['Well ID'].str.contains("2005-5-001")]
print(dataframe1)

grouped = data.groupby('Well ID')

for name,group in grouped:
   print (name)
   print (group)
   group.plot(x='Date', y='Manual Computed Water Level (masl)', title = name)
   plt.xlabel('Date')
   
   plt.ylabel('Water Level')
   plt.title("Well " + name + ' (Water Level Vs Date)')
   plt.legend(['Water Level Over Time'])
   plt.savefig(name, dpi=300, bbox_inches='tight')
   plt.close()
