import os
# d:\Python_Kursy\Python_Udemy\zadanie1.txt
filename = input("Please, enter the path to file from previous task: ")

while True:
    if os.path.isfile(filename):
        webaddresses = []
        file = open(filename,'r')
        for line in file:
            line = line.replace('\n','')
            webaddresses.append(line)

            if line.endswith('.pl'):
                print("adres",line,"jest adresem z Polski")
            else:
                print("adres",line,"nie jest adresem z Polski")
                 
        
        file.close()
        print(webaddresses)
        break
    else:
        filename = input("Please, enter correct path: ")
