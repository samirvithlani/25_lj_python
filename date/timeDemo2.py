from datetime import time as tm
from datetime import datetime
t=tm(14,30,35)
print(t)
print(t.minute)
print(t.second)
print(t.hour)

#timestamp
now = datetime.now()
print(now.timestamp()) #1970 1st january

dt = datetime.fromtimestamp(0) #1ms pass
print(dt)

dtnow = datetime.fromtimestamp(now.timestamp())
print(dtnow)

#ctime
print(now.ctime())
#isofomrmate
print(now.isoformat())

#replace
new_date = now.replace(year=2032,month=1)
print(new_date)
