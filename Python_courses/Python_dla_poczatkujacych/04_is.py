a='kartka'
b='k'
b+='artka'
#kontrolne wyświetlenie zmiennych
print ('a = ', a)
print ('b = ', b)
#sprawdzam czy a == b
print ('Is a == b ?',a==b)
#sprawdzam czy a i b to ta sama zmienna (operator is)
print ('Is a == b ?',a is b)
#is sprawdza czy 2 zmienne są identyczne - identyfikator zmiennej zwraca funkcja id()
print(a,id(a),b,id(b),a is b)
