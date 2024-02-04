import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)
final_data=dataframe[dataframe['reservation_status']=='Check-Out']
final_data=final_data[['reservation_status','country']]
final_data=final_data.groupby('country').agg({'reservation_status':"count"}).rename(columns={'reservation_status':'Bookings'}).reset_index()
final_data=final_data.sort_values('Bookings',ascending=False).reset_index()
final_data=final_data.loc[0:11,:]
sns.barplot(data=final_data, x='country', y='Bookings')
plt.title("Distribution of booking over country")
plt.xlabel("Country codes")
plt.ylabel("No. of Bookings")
plt.show()
