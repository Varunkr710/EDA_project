import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)
sns.barplot(data=dataframe,x='hotel', y='is_canceled')
plt.title("Cancellations over Hotel Types")
plt.xlabel("Hotel types ")
plt.ylabel("No. of cancellations")
plt.show()