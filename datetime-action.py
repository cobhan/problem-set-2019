#8 Write a program that outputs today’s date and time in the format “Monday, January 10th 2019 at 1:15pm”.

import datetime as dt #import pythons built in datetime module

now = (dt.datetime.now()) #using now call we can get the time in object form

day = now.strftime("%A") #strftime lets us convert date/time etc to equivalent string
month = now.strftime("%B")
monthdate = now.strftime("%-d")
year = now.strftime("%Y")
time = now.strftime("%-I %p")

print(day, month, monthdate, year, "at", time) #join together and print

#reference https://www.programiz.com/python-programming/datetime/strftime