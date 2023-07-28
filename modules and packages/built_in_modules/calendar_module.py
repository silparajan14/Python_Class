#the calendar module allows output calendars like the program and provides additional fns related to calendar

import calendar

#(donot name "calendar" as file name)

#to print calendar of certain month
# year = int(input("year : "))
# month = int(input("month : "))
# a = calendar.month(year,month)
# print(a)

#to get all months
# year1 = int(input("year : "))
# b = calendar.calendar(year1)
# print(b)

#b = calendar.calendar(year,w,l,c)
# here
#         w  = width
#         l = length
#         c = distance between the 2 months
# b = calendar.calendar(2023,1,2,5)
# print(b)

#isleap() :
# year = int(input("year : "))
# a = calendar.isleap(year)
# print(a)

#TextCalendar : to customise our calendar according to us
# year = int(input("year : "))
# c = calendar.TextCalendar(calendar.FRIDAY)
#print(c.formatyear(year))   #if we need to customise the whole year
#print(c.formatmonth(2010,9))   #if we need to customise the month only

#help(calendar)



