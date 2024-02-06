import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
data=pd.read_csv(path)                        # loading the dataset
Final_data=data[['lead_time','stays_in_weekend_nights','stays_in_week_nights','days_in_waiting_list','is_repeated_guest', 'previous_cancellations','booking_changes']]
sns.heatmap(data=Final_data.corr(), annot=True, cmap="coolwarm")
plt.show()