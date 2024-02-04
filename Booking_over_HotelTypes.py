import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)
New_dataframe=dataframe.loc[dataframe['reservation_status']=='Check-Out']
New_dataframe=New_dataframe.groupby('hotel').agg({'reservation_status':'count'})
sns.barplot(data=New_dataframe, x=New_dataframe.index, y='reservation_status')
plt.title("Booking over hotel types")
plt.xlabel("Hotel types")
plt.ylabel("No. of bookings")
plt.show()