quote = ('A good programmer is someone who always looks both ways before crossing a one-way street')
print(quote)

print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find('one'))
print(quote.replace('one','1'))
print(quote.replace('one','1').replace('both','2')) 
print(quote.split(' '))
print(quote.isdigit()) #sprawdza czy tekst jest liczba
print(quote.isdecimal()) #sprawdza czy tekst jest liczba dziesietna
print(quote.isalpha()) #sprawdza czy napis jest bez cyfr
print(quote.isalnum()) #sprawdza czy napis jest z literami i cyframi

s = '123'
print(s)
print(s.isdigit())
print(s.isnumeric())
print(s.isdecimal())
 
 
s = '½'
print(s)
print(s.isdigit())
print(s.isnumeric())
print(s.isdecimal())
 
s = '³'
print(s)
print(s.isdigit())
print(s.isnumeric())
print(s.isdecimal())
