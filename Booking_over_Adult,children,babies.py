import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)
dataframe.columns
new_data=dataframe[['hotel','adults', 'children', 'babies']]
new_data=new_data.groupby('hotel').agg({'adults':'sum','children':'sum','babies':'sum'})  # group the data by hotel types
new_data.plot(kind='bar',rot=0)
plt.title("Hotel types vs adults, children, babies")
plt.xlabel("Hotel Types")
plt.ylabel("No. of persons")
plt.show()
