import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="/content/drive/MyDrive/Hotel Bookings.csv"
data=pd.read_csv(path)               # loading our dataset
data=data[data['reservation_status']=='Check-Out']   # removing the cancellated bookings
data=data.groupby('meal').agg({'reservation_status':'count'}).rename(columns={'reservation_status':'No. of customers'}).reset_index() # grouping the data
sns.barplot(data=data,x='meal',y='No. of customers')
plt.title("Meal vs customers")
plt.xlabel('Meal types')
plt.ylabel('No. of Customers')
plt.show()