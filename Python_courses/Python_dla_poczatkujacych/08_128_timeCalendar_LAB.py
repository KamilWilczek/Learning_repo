import time

print('data i godzina w unix', time.time())

print('date and time readable for human', time.asctime(time.localtime(time.time())))

import calendar

print('Wife birthday', calendar.month(1992,6))
calendar.setfirstweekday(6)
print("Son's birthday", calendar.month(2019,10))
print('is 2000 a leap year?', calendar.isleap(2000))
print(calendar.calendar(2020))
