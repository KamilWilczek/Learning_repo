import random

min = 1
max = 6



##dice = random.randint(min,max)
##if dice == 1:
##    print("   \n   \no")
##elif dice == 2:
##    print("  o\n   \no")
##elif dice == 3:
##    print("  o\n o \no")
##elif dice == 4:
##    print("o o\n   \no o")
##elif dice == 5:
##    print("o o\n o \no o")
##elif dice == 6:
##    print("o o\no o\no o")

##import random
## 
##min = 1
##max = 6
## 
### sciany kostki
##s1 = "o"
##s2 = " o\n\no"
##s3 = "  o\n o\no"
##s4 = "o o\n\no o"
##s5 = "o o\n o\no o"
##s6 = "o o o\n\no o o"
## 
### losowanie wyniku
##dice = random.randint(min, max)
## 
### inicjacja listy scian kosci z pustym elementem zerowym w zwiazku z indeksacja pythona
##sides = ["", s1, s2, s3, s4, s5, s6]
## 
##print(sides[dice])

dices = []

for i in range(5):
    dices.append(random.randint(min,max))
dices.sort()
print(dices)
