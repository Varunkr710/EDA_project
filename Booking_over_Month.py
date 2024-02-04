import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)
final_data=dataframe[dataframe['reservation_status']=='Check-Out']
final_data=final_data[['reservation_status','arrival_date_month']]
final_data=final_data.groupby('arrival_date_month').agg({'reservation_status':"count"}).rename(columns={'reservation_status':'Total Hotels'})
#sns.barplot(data=color, x='arrival_date_month', y='Total Hotels')
final_data.plot(kind='bar', rot=90)
plt.title("Booking over different months")
plt.xlabel("Months")
plt.ylabel("No. of bookings")
plt.show()