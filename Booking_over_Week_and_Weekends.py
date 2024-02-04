import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
path="Hotel Bookings.csv"
dataframe=pd.read_csv(path)

def Convert(x,y,z):
    data={'April': 4, 'August':8, 'December':12, 'February':2, 'January': 1, 'July':7, 'June':6,
       'March': 3, 'May':5, 'November':11 , 'October':10, 'September':9}
    temp=datetime.datetime(x,data[y],z)
    if int(temp.strftime("%u"))>5:
       return "Weekend"
    return "Weekdays"
require=dataframe[['hotel','arrival_date_day_of_month','arrival_date_month', 'arrival_date_year' ]]
require.loc[:,"Day type"]=require.apply(lambda x : Convert(x['arrival_date_year'],x['arrival_date_month'],x['arrival_date_day_of_month']),axis=1)
next=require.groupby("Day type").agg({'arrival_date_day_of_month':'count'})
sns.barplot(x=next.index ,y='arrival_date_day_of_month' , data=next)
plt.title("Distribution of booking over weekdays and weekends")
plt.xlabel("Day type")
plt.ylabel("No. of bookings ")
plt.show()
