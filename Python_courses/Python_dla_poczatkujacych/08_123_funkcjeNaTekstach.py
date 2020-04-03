line = 'this IS a very STRANGE text'
print(line)
print(line.capitalize())

print(line.title())

print(line.upper())

print(line.lower())

print(line.swapcase())

print(line.casefold())

line1 = 'der Fluß'
print(line1.lower())
print(line1.casefold())

line2 = 'ŻÓŁĆ'
print(line2.lower())
print(line2.casefold())
print(line2.replace('Ż','Z').replace('Ó','O').replace('Ł','L').replace('Ć','C').lower())

print(line.count('e'))

print(line.find('e'))
print(line.rfind('e'))

print(line.index('e'))
print(line.rindex('e'))

print(line.find('p'))
##print(line.index('p'))
##Traceback (most recent call last):
##  File "D:/Python_Kursy/Python_Udemy/08_123_funkcjeNaTekstach.py", line 33, in <module>
##    print(line.index('p'))
##ValueError: substring not found

#w shellu
print('e' in line)
print('p' in line)

print(line.startswith('this'))
print(line.startswith('THIS'))
print(line.endswith('text'))
line3 = """this is a long text
that spans multiple lines
but should be somehow presented in python"""

print(line3)
print(line3.count('\n'))

import string
print(string.ascii_letters)
print(string.digits)

line4 = 'this is the end of this lesson'
print(line4.split(' '))
list = line4.split(' ')
print(list)

##print(list.join(' '))
##Traceback (most recent call last):
##  File "D:/Python_Kursy/Python_Udemy/08_123_funkcjeNaTekstach.py", line 62, in <module>
##    print(list.join(' '))
##AttributeError: 'list' object has no attribute 'join'

print(' '.join(list))
