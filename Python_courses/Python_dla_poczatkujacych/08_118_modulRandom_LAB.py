import random
##i=0
##for i in range(1,11):
##    print("Losowa liczba nr. ", i , 'to ', random.choice(range(1,100)))
##    i +=1

##number2 = random.randrange(1,100)
##counter = 1
##number1 = 0
##while number2 != number1:
##    number1 = random.randrange(1,100)
##    print("Step %3d, number %3d, looking for %3d" % (counter, number1, number2))
##    counter += 1

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("====Grupa %d====" % (groupNumber))
    print(countries[i])

random.shuffle(countries)
 
##print (countries)
## 
##groupNumber = 0
## 
##for country in countries:
##    if countries.index(country) % 4 == 0:
##        groupNumber += 1
##        print ("----- GROUP {} -----".format(groupNumber))
##    print (country)
