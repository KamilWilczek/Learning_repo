#dictionary = {'key1':'value1','key2':'value2'}
CountryLeaders = {'PL':'Duda','US':'Trump'}

print(CountryLeaders)

print(CountryLeaders['US'])

CountryLeaders['DE'] = 'Merkel'

print(CountryLeaders)

print(CountryLeaders.keys())
print(CountryLeaders.values())
print(CountryLeaders.items())

#print(CountryLeaders.popitem()) - pozwala przechodzic krok po kroku z elementu na element usuwajac go
print(CountryLeaders.setdefault('FR','Macron'))
'''
gdyby nie bylo klucza FR to wyswietl wartosc Macron
i dodatkowo wpisuje klucz i wartosc w slownik
'''
print(CountryLeaders.get('RU')) #zwraca wartosc a jak nie ma to nie dopisuje

NewLeaders = {'RU':'Putin','DE':'Schultz'}
print(NewLeaders)
CountryLeaders.update(NewLeaders)
'''
dodaje slowniki, istniejace wartosci podmienia, nieistniejace dodaje
'''
print(CountryLeaders)

