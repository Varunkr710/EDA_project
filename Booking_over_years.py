import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)
color=dataframe[dataframe['reservation_status']=='Check-Out']   # removing the cancelled booking
color=color[['reservation_status','arrival_date_year']]
color=color.groupby('arrival_date_year').agg({'reservation_status':"count"}).rename(columns={'reservation_status':'Bookings'}).reset_index()
color['arrival_date_year']=color['arrival_date_year'].astype(str)        # converting the arrival_date_year to string
sns.lineplot(data=color, x='arrival_date_year',y='Bookings')
plt.title("Booking vs years")
plt.xlabel("Timeline")
plt.ylabel("No. of bookings")
plt.show()