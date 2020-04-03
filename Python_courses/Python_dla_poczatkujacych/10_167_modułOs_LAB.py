import os
import time

dir = input('Please enter path to directory: ')

if os.path.isdir(dir):
    file = input('Give file name: ')
    path = os.path.join(dir, file)
    if os.path.exists(path):
        print("Below will be printed file properties:")
        print("\nLast modify date is:",time.localtime(os.path.getmtime(path)))
        print("\nFile size is (KB): ",os.path.getsize(path))
        print("\nCurrent directory is:",os.getcwd())
        print("\nThe absolute path is: ", os.path.abspath(path))
    else:
        print("File does not exists")
else:
    print('Provided name is not directory path')



#D:\Python_Kursy\Python_Udemy
    


test = r'D:\Python_Kursy\Python_Udemy'
print("1",os.path.exists(test))
print("2",os.path.isfile(test))
