"""
Zapisz poniższe polecenie if w postaci uproszczonej:

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)
"""
price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

price = price - bonus if bonus_granted else price
print(price)

"""
Zapisz poniższe polecenie if w postaci uproszczonej:

rating = 5
 
if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')
"""

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')

"""
Ktoś był kiedyś niezadowolony, bo w kursie jest za mało polskich akcentów, więc...
posłuchaj piosenki De Mono - Niedziela będzie dla nas - https://www.youtube.com/watch?v=lmn0Qf1_eI4 
(możesz też skorzystać z oryginalnej wersji: Niebiesko Czarnych: https://www.youtube.com/watch?v=Fxkhe8GqYkc)
Napisz program, który:
zapisze w zmiennej today_weekday nazwę dzisiejszego dnia tygodnia
bazując na pierwszej zwrotce piosenki serią poleceń if/elif/.../else ustali co dzisiaj powinieneś robić
Przepisz powyższy program stosując składnie uproszczona polecenia if
"""

from datetime import datetime
today_weekday = datetime.now().strftime('%A')
print(today_weekday)

if today_weekday == 'Monday':
    print("I'm helping mom")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("You're doing laundry")
elif today_weekday == 'Thursday':
    print("I'm on duty")
elif today_weekday == 'Friday':
    print('I have two meetings')
elif today_weekday == 'Saturday':
    print("You have a class")
else:
    print("Sunday is for us")

print("I'm helping mom") if today_weekday == 'Monday' else print("You're doing laundry") if \
    today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else print("I'm on duty") if \
    today_weekday == 'Thursday' else print('I have two meetings') if today_weekday == 'Friday' else \
    print("You have a class") if today_weekday == 'Saturday' else print("Sunday is for us")


