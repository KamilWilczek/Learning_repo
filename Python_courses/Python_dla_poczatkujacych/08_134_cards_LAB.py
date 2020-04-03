colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

allCards = []

for color in colors:
    for figure in figures:
        allCards.append(color + ' ' + figure)
        #allCards.append("%s %s" % (color, figure))

print(allCards)

import random

random.shuffle(allCards)
print(allCards)
print('---------------------------------------------')

player1 = []
player2 = []

max = len(allCards)
for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 2--------')
print(player2)     

print('\n')
print('_________Sposób nr2._________')
print('\n')

player1 = allCards[:12]
player2 = allCards[12:]
 
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 1--------')
print(player2)

##import random
## 
##colors = ["\u2661", "\u2662", "\u2663", "\u2660"]    #wyswietlenie symboli Unicode
## 
##figures = ["A", "K", "Q", "J", "10", "9"]
## 
### tablice
##allCards = []
##player1 = []
##player2 = []
## 
### zapelnienie talii kartami
##for color in colors:
##    for figure in figures:
##        allCards.append(figure + color)
## 
### wyswietlenie kart
##print(allCards)
## 
### potasowanie
##random.shuffle(allCards)
## 
##print("Potasowane karty:\n", allCards)
## 
##print("\n-------------------------------------------- pierwszy sposob ---------------------------------------- \n")
##maxCards = len(allCards)
## 
##for i in range(maxCards):
## 
##    if i % 2 == 0:
##        player1.append(allCards[i])
##    else:
##        player2.append(allCards[i])
## 
##print("Karty pierwszego gracza to", player1)
##print("Karty drugiego gracza to", player2)
## 
##print("\n---------------------------------------- drugi sposob ---------------------------------------- \n")
## 
##player1_2nd = allCards[:12]
##player2_2nd = allCards[12:]
## 
##print("Karty pierwszego gracza", player1_2nd)
##print("Karty drugiego gracza", player2_2nd)
