def GiveWorkingDay(year, month, day):
    #prints the nearest working day date
    from datetime import date
    from datetime import timedelta

    #day = date.today()
    #day = date(2017,10,1)
    #day = date(2017,9,30)
    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print('working day for' , day, 'is',workingday)

    return

GiveWorkingDay(2017,9,30)
GiveWorkingDay(2020,1,19)
GiveWorkingDay(year=2017,month=12,day=6)
GiveWorkingDay(day=6,month=12,year=2018)
