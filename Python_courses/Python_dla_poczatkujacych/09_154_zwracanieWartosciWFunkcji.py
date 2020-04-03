from datetime import date
from datetime import timedelta
#def GiveWorkingDay(year,month=1,day=1):
def GiveWorkingDay(year=date.today().year,\
                   month=date.today().month,\
                   day=date.today().day):
    #prints the nearest working day date
    

    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day


    return workingday


nextworkingday = GiveWorkingDay(2017,9,2)
print('Next working day after',2017,9,2,'is',nextworkingday)
nextworkingday = GiveWorkingDay()
print('Next working day after today is',nextworkingday)

print('Next workingday after today is',GiveWorkingDay())

