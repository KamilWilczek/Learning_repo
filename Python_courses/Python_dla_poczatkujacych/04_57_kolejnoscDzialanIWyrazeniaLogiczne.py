nr = 42
print(nr)
print(nr*5)
print(nr*5+50)
print((nr*5+50)*20)
print((nr*5+50)*20+1019)
print((nr*5+50)*20+1019-1992)
number = ((nr*5+50)*20+1019-1992)


print("moj numer buta: ",number//100)
print("moj wiek: ",number % 100)

l = 8
liczba = (l*2+10)/2-l
print(liczba)

print("2+2*2 = ",2+2*2)
print("7+7/7+7*7-7 = ",7+7/7+7*7-7)
print('44444444444444444444444444444444444444444444')
obecnosc = 0.85
srednia = 3.5
praca = False

zaliczenie = obecnosc*100 >= 80 and srednia >= 3.0 or praca
print(zaliczenie)

print('555555555555555555555')
obecnosc = 0.85
srednia = 3.5
praca = False

zaliczenie = obecnosc*100 >= 80 and srednia >= 3.0 and praca
print(zaliczenie)
print('6666666666666666666666666666')
obecnosc = 0.40
srednia = 2.5
praca = True

zaliczenie = obecnosc*100 >= 80 and srednia >= 3.0 or praca
print(zaliczenie)
print('6a6a6a6a6a6a')
obecnosc = 0.40
srednia = 3.5
praca = True

zaliczenie = obecnosc*100 >= 80 and srednia >= 3.0 and praca
print(zaliczenie)

presence = 0.85
note =3.5
finalWorkOK = False
print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)
presence = 0.4
note =2.5
finalWorkOK = True
print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)
