Tax = (4,7,8,23)
print(Tax)
print(Tax[2])
print(Tax[-1]) #wywolywanie od konca

#tuple.index(element) - na której pozycji znajduje się obiekt. 7 jest na 1 pozycji licząc od 0
print(Tax.index(7))
#tuple.count(element) - ile razy obiekt występuje w liście np. 8 występuje 1 raz
print(Tax.count(8))
#max(tuple) - maksymalna wartość w liście
print(max(Tax))
#Tax.revert() - krotek nie można modyfikować, aby to robić trzeba zamienić ją w listę
TaxList = list(Tax) #zamiana krotki w listę
TaxList.append(30) #dodanie elementu do listy
NewTax = tuple(TaxList) #zamiana listy w krotkę

print(Tax)
print(TaxList)
print(NewTax)

(tax1,tax2,tax3,tax4) = Tax #przypiaslo wartosci z Tax do zmiennych
print(tax1,tax2,tax3,tax4)

##############################################################
a=1
b=10
print("a =",a,"\tb =",b)
'''
a=b
b=a
print("a =",a,"\tb =",b) #stracona zostala wartosc "a", rozwiazaniem jest zmienna temp

a = 1 	b = 10
a = 10 	b = 10
'''
#################################################################
#temp = a
#a = b
#b = temp
#lub
(a,b)=(b,a)
print("a =",a,"\tb =",b)

