import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
data=pd.read_csv(path)         # loading our dataset
data=data[data['reservation_status']=='Check-Out'] # removing the cancelled booking from our dataset
sns.boxplot(data=data,y="lead_time")               # ploting our data
plt.title("Distribution of Lead Time")
plt.ylabel("Time")
plt.show()