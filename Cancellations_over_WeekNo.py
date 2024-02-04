import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)
money=dataframe[['arrival_date_week_number','reservation_status']]
money=money[money['reservation_status']=='Canceled']
money=money.groupby("arrival_date_week_number").agg({'reservation_status':"count"})
plt.figure(figsize=(20,10))
sns.barplot(data=money,x='arrival_date_week_number',y='reservation_status')
plt.title("Cancellation over week numbers")
plt.xlabel("Week numbers ")
plt.ylabel("No. of cancellations")
plt.show()
