string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for number in range (1,11):
    print(string_A)

print("------------------------------------")

for number in range (1,10):
    if number %2 == 0:
        print(string_B)
    else:
        print(string_A)

print("------------------------------------")

for number in range (1,10):
    print("x"*number)

print("------------------------------------")

for number in range (1,10):
    if number %2 == 0:
        print("x"*number)
    else:
        print("o"*number)
