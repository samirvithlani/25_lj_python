# import datetime
# import time
# import calendar

from datetime import date
today = date.today()
print(today)
print(type(today))

#access year month day
print(today.day)
print(today.year)
print(today.month)
print(today.weekday())
print(today.isoweekday())

#cust date
d1 = date(2025,12,31)
print(d1)
