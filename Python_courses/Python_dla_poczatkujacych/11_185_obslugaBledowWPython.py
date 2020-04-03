import os
import sys
# d:\Python_Kursy\Python_Udemy\data_output\obslugaBledow.txt
# d:\Python_Kursy\Python_Udemy\testy\obslugaBledow.txt
line = input("What's the best course price according to you?: ")

dirname = input("Where to save the file?: ")
#file_path = os.path.join(dirname, 'obslugaBledow.txt')


try:
    file = open(dirname, 'w')
    file.write(line)
    file.close()
    value = int(line)
    print("The value saved in this file is %d" % (value))
except FileNotFoundError as e:
    print("Error opening file:", dirname)
except ValueError as e:
    print("The value entered cannot be converted to a number:", line)
except:
    print("SORRY - WE HAVE AN ERROR", sys.exc_info()[0])
else:
    print("Actions completed successfully")


'''
Traceback (most recent call last):
  File "D:/Python_Kursy/Python_Udemy/11_185_obslugaBledowWPython.py", line 9, in <module>
    file = open(dirname, 'w')
FileNotFoundError: [Errno 2] No such file or directory: 'd:\\Python_Kursy\\Python_Udemy\\testy\\obslugaBledow.txt'
'''
