import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
mon=pd.read_csv(path)                                        # loading the dataset
Read=mon[['customer_type','lead_time','stays_in_weekend_nights','stays_in_week_nights','days_in_waiting_list','booking_changes']]
sns.pairplot(data=Read,hue='customer_type')
plt.show()