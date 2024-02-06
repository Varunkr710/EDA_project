import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)      # loading the dataset
final_data=dataframe[dataframe['reservation_status']=='Check-Out'] # removing the cancelled booking
final_data=final_data[['reservation_status','country']]            # taking the two columns only reservation status and country
final_data=final_data.groupby('country').agg({'reservation_status':"count"}).rename(columns={'reservation_status':'Bookings'}).reset_index() # grouping by coutry
final_data=final_data.sort_values('Bookings',ascending=False).reset_index()   # sorting the values descending
final_data=final_data.loc[0:11,:]   #Selecting the top 12 entries
sns.barplot(data=final_data, x='country', y='Bookings')   #ploting the graph
plt.title("Booking vs CountryCodes")
plt.xlabel("Country codes")
plt.ylabel("No. of Bookings")
plt.show()
