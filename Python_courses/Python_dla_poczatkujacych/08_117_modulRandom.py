import random
#losuje liczbe calkowita w pelnym zakresie od 1 do 100 
print("One random number:", random.randint(1,100)) # 1 <= N <= 100
print("\n")
#losuje jeden element z zakresu
print("Choosing random number from a range", random.choice(range(1,100)))
print("\n")
#to samo co wyzej ale krotsze
print("Choosing random number from a range - easier", random.randrange(1,100))
print("\n")
#losowo miesza zawartosc listy
list = ["John","Ann","Peter","Susan","Emily","Greg","Chris"]
random.shuffle(list)
print("Reordered list:",list)
print("\n")

print("Just a random float", random.random())
print("\n")
