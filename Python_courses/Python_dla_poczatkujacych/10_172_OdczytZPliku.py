print("-----------Sposób 1-----------")

file = open("d:\\Python_Kursy\\Python_Udemy\\joke.txt","r")

content = file.read()
print(content)
file.close()

print("-----------Sposób 2-----------")

with open("d:\\Python_Kursy\\Python_Udemy\\joke.txt","r") as file:
    content = file.read()
    print(content)

print("-----------Sposób 3-----------")
#dla dużych plików

with open("d:\\Python_Kursy\\Python_Udemy\\joke.txt","r") as file:
    for line in file:
        print(line)

print("-----------Sposób 4-----------")

file = open("d:\\Python_Kursy\\Python_Udemy\\joke.txt","r")
for line in file:
        print(line)
file.close()

print("-----------TAK NIE ROBIC-----------")
file = open('d:\\Python_Kursy\\Python_Udemy\\joke.txt','r')
for line in file.readlines():
    print(line)
file.close()

print("-------------------------------")
#dla dużych plików
file = open('d:\\Python_Kursy\\Python_Udemy\\joke.txt','r')
fragment = file.read(10) #chemy przeczytac maks 10 bajtów
while fragment:
    print(file.tell(),fragment)
    fragment = file.read(10)

file.close()
