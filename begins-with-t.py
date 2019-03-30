# Write a program that outputs whether or not today is a day that begins with the letter T. An example of running this program on a Thursday is as follows.

from datetime import date
import calendar
my_date = date.today()
today = (calendar.day_name[my_date.weekday()])
if today == ("Thursday" or "Tuesday"):    
    print("Yes - today begins with a T.")
else:
    print("No - today does not begin with a T.")

# https://www.pythonprogramming.in/get-the-day-of-week-from-given-a-date-in-python.html