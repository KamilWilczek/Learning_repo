countries = ['FR','US','DE','RU']
print(countries)
print(countries[1])
countries[1] = 'GB'
print(countries)
countries.append('PL')
print(countries)
countries.insert(2,'ES')
print(countries)
countries.remove('RU')
print(countries)
countries.sort()
print(countries)
countries.reverse()
print(countries)
print(countries.pop(2))
print(countries)
print(countries.index('PL'))
#print(countries.index('US'))
#    Traceback (most recent call last):
#  File "D:/Python_Kursy/Python_Udemy/05_59_listy.py", line 19, in <module>
#    print(countries.index('US'))
#ValueError: 'US' is not in list
print(countries)
print(countries.count('DE'))
print('\n')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('\n')
newList = ['FI','SE']
print('newList = ',newList)
countries.extend(newList)
print(countries)
print('\n')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('\n')
countriesCopy = countries
countriesCopy.clear()
print(countries)
print(countriesCopy)
print('\n')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('\n')
countries = ['PL','GB','ES','DE','FI','SE']
print(countries)
countriesCopy = countries.copy()
countriesCopy.clear()
print(countries)
print(countriesCopy)


