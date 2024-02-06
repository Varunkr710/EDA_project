import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
data=pd.read_csv(path)            # loading the dataset
data=data[data['reservation_status']=='Check-Out']  # removing the cancelled bookings
data=data.groupby("total_of_special_requests").agg({'reservation_status':'count'})  # grouping the special requests
sns.barplot(data=data,x="total_of_special_requests",y='reservation_status')        # plotting the graph using barplot
plt.title("No. of Requests vs Customers")
plt.ylabel("No. of customers")
plt.xlabel("No. of Requests")
plt.show()