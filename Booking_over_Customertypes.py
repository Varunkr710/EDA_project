import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)
final_data=dataframe[dataframe['reservation_status']=='Check-Out']
final_data=final_data[['reservation_status','customer_type']]
final_data=final_data.groupby('customer_type').agg({'reservation_status':"count"}).rename(columns={'reservation_status':'Bookings'})
sns.barplot(data=final_data, x='customer_type', y='Bookings')
plt.title("Booking_on_customerTypes")
plt.xlabel("Customer Types")
plt.ylabel("No. of Bookings")
plt.show()