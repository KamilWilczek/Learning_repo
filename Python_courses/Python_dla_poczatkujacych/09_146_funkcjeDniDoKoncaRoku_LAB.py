def DaysToEndOfYear():
    #print how many days left till end of year
    from datetime import date

    day = date.today()
    current_year = day.year
    date_end_year = date(current_year,12,31)
    delta = date_end_year - day
    print(delta.days)
    return

DaysToEndOfYear()

def EndofYear():
    import time, calendar
    ctime = time.localtime(time.time())
    daysleft = 365 + calendar.isleap(ctime.tm_year) * 1 - ctime.tm_yday
    print ('There are', daysleft ,'days left.')
    return

EndofYear()
