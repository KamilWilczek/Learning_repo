#  playing with time

import time

print("Current time is... unix epoch", time.time())
print("\n")
print("Current time is... tuple", time.localtime(time.time()))
print("\n")
print("Current time is... for human",   time.asctime(time.localtime(time.time())))
print("\n")
print("Current time is... for human",   time.localtime(time.perf_counter()))
print("\n\n\n\n\n\n")

#  playing with calendar

import calendar

print("                                         ")
print(calendar.month(2020,1,w=5,l=2))
print('-----------------------------------------')
print(calendar.month(2020,1))
print('-----------------------------------------')
print('week day is',calendar.weekday(2020,1,14))
print('-----------------------------------------')
calendar.setfirstweekday(6) # wplywa tylko na to jak kalendarz jest rysowany
print('-----------------------------------------')
print(calendar.month(2017,9))
print('-----------------------------------------')
print('week day is',calendar.weekday(2020,1,14))
print('-----------------------------------------')
print('is 2020 a leap year?', calendar.isleap(2020))
print('-----------------------------------------')
print('Leap days 2000-2017', calendar.leapdays(2000,2017))
#od 2000 włącznie do 2020 wyłącznie
print('Leap days 2000-2020', calendar.leapdays(2000,2020))
print('Leap days 2000-2021', calendar.leapdays(2000,2021))
print('-----------------------------------------')

print(calendar.calendar(2020))
