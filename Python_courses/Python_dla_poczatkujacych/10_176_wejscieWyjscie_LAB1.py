import os

webaddresses = []

line = input("Please, give the www address: ")

while len(line) > 0:
    webaddresses.append(line)
    line = input("Please, give another www address: ")
    
dirname = os.getcwd()
name = input("Type filename: ")
filename = name+'.txt'

filepath = os.path.join(dirname, filename)

file = open(filepath, "w")
for address in webaddresses:
    file.write(address+"\n")
file.close()

