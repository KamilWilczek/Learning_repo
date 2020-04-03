
'''
    Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
    Zakladamy ze:
    -liczba mrugniec na minute to 20
    -liczba minut w godzinie to 60
    -liczba godzin w dobie 24
    -liczba lat (czyli nasz X) 50
    Uwaga: jezeli przyjac ze spimy 8 godzin to liczba godzin na dobe
    powinna wynosic 16
'''
# liczba mrugnięć okiem na minutę
blinksPerMin = 20

#liczba minut na godzinę i liczba godzin w dobie
MinInHour = 60
hoursInDay = 24
days_in_year = 365

#liczba lat
years = 50

#liczba mrugnięć w ciągu X lat
print(blinksPerMin*MinInHour*hoursInDay*days_in_year*years)

'''
    #definitionOfVariables
    daysOfWorkPerMonth = 20 - w print "Month" jest małą literą
    monthsInYear = 12
    vacation = 26 - w print "vacation" jest wielką literą
    yearsOfWOrk = 40
    #result
    print((daysOfWorkPermonth * monthsInYear - Vacation)*yearsOfWOrk)
'''
