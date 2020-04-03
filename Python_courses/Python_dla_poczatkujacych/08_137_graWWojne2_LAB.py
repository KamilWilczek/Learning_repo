colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

import random
random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

for i in range(len(allCards)):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
print('---------PLAYER 1-------')
print(player1)
print('---------PLAYER 2-------')
print(player2)
n=0
while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    stock = []
    if card1["Power"] == card2["Power"]:
        while card1['Power'] == card2['Power']:
            print('=WAR! \t %d \t %d \t' % (card1["Power"], card2["Power"]))
            stock.append(card1)
            stock.append(card2)
            
            if len(player1) < 2:
                player2.extend(stock)
                player2.extend(player1)
                player1 = []
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
                break
            elif len(player2) < 2:
                player1.extend(stock)
                player1.extend(player2)
                player2 = []
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
                break
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stock.append(card1)
                stock.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                
                
        else:
            if card1['Power'] > card2['Power']:
                stock.append(card1)
                stock.append(card2)
                player1.extend(stock)
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
            else:
                stock.append(card1)
                stock.append(card2)
                player2.extend(stock)
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    elif card1["Power"] > card2["Power"]:
            player1.append(card1)
            player1.append(card2)
            #print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
            print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
            player2.append(card2)
            player2.append(card1)
            #print('PLAY-2 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
            print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
 
    n += 1
    print(n)
if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    ptint('PLAYER 2 WON!!!!')
##    Traceback (most recent call last):
##  File "D:\Python_Kursy\Python_Udemy\08_137_graWWojne_LAB.py", line 37, in <module>
##    card2 = player2.pop(0)
##IndexError: pop from empty list


