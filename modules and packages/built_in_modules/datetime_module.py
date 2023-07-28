#the python datetime module supplies classes to work with date and time.
#these classes provide a number of fns to deal with dates, times, and time intervals.

import datetime

#date() :it is a constructor to convert data into a date format
# mydate = datetime.date(1997,2,14)  #year,month,day
# print(mydate)

#date.today() :
# today = datetime.date.today()
# print("Today's date is ",today)
# #to get results separately
# print("current year ",today.year)
# print("current month ",today.month)
# print("current day ",today.day)

#datetime.now() : used to display current date and time
# today = datetime.datetime.now()
# print("current date and time is ",today)

#find the difference between 2 days
# date1 = datetime.datetime(2022,11,1)
# date2 = datetime.datetime(2022,11,4)
# diff = date2 - date1
# print(diff)

#timedelta() : we need to import it
from datetime import timedelta

#2 days after today
# date = datetime.date.today()
# date += timedelta(days = 2) #after 2days
# print("date after 2 days is ",date)

#find the date before 20 days
# date = datetime.date.today()
# date -= timedelta(days = 20) #before 20days
# print("date before 20 days is ",date)













