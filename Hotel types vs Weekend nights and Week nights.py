import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)                       # loading the dataset
dataframe.columns
new_data=dataframe[['hotel','stays_in_week_nights', 'stays_in_weekend_nights']]
new_data=new_data.groupby('hotel').agg({'stays_in_week_nights':'sum','stays_in_weekend_nights':'sum'}) # adding the stays in week nights and week days
new_data.plot(kind='bar',rot=0)
plt.title("Hotel types vs Weekend nights and Week nights ")
plt.xlabel("Hotel Types")
plt.ylabel("No. of nights")
plt.show()