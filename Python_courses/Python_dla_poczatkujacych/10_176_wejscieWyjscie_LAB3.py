import os
# d:\Python_Kursy\Python_Udemy\zadanie1.txt
filename = input("Please, enter the path to file from previous task: ")

while True:
    if os.path.isfile(filename):
        webaddresses = []
        name2 = os.path.join(os.path.dirname(filename),'webs_pl.txt')
        name3 = os.path.join(os.path.dirname(filename),'webs_other.txt')

        file = open(filename,'r')
        file2 = open(name2, 'w')
        file3 = open(name3, 'w')
        for line in file:
            line = line.replace('\n','')
            #webaddresses.append(line)
            if line.endswith('.pl'):
                file2.write(line+"\n")
                print("adres",line,"jest adresem z Polski")
            else:
                
                file3.write(line+"\n")
                print("adres",line,"nie jest adresem z Polski")
        file.close()
        file2.close()
        file3.close()
        print(webaddresses)
        break
    else:
        filename = input("Please, enter correct path: ")
