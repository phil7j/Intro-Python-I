"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

"""

from datetime import datetime
import sys
import calendar

# def date_func(month=10, year=2019):
#     print(calendar.month(year, month))


month = (input("Month?"))

year = (input("Year?"))


if month == "" and year == "":
    print(calendar.month(datetime.now().year, datetime.now().month))
elif month == "" or year == "":
    if month != "":
        print(calendar.month(datetime.now().year, int(month)))
    elif year != "":
        print(calendar.month(int(year), datetime.now().month))
elif len(month) == 2 and len(year) == 4:
    print(calendar.month(int(year), int(month)))
else:
    print("Please enter with format MM and YYYY and use numbers!")
    exit()
