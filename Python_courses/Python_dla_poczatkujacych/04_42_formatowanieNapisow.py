message1 = 'Processing file %s'
print(message1 % ('file_1.text'))
message2 = "File %s has size %d KB"
print(message2 % ('file_txt',100))
#print(message2 % (100,'file_txt')) - nie mozna zamienic kolejnosci
# %s - string, %d - liczba
'''
Traceback (most recent call last):
  File "D:/Python_Kursy/Python_Udemy/04_42_formatowanieNapisow.py", line 5, in <module>
    print(message2 % (100,'file_txt'))
TypeError: %d format: a number is required, not str
'''
message3 = 'File %20s has size %10d KB' #%20s rezerwuje 20 znakow na string
print(message3 % ('file1.txt',100))
message4 = 'Processing file {0:s}'
print(message4.format('file1.txt'))
message5 = 'File {0:s} has size {1:d}'
print(message5.format('file1.txt',100))
message55 = 'File {1:s} has size {0:d}'
print(message55.format(100,'file1.txt'))
message6 = 'File {0:20s} has size {1:10d}'
print(message6.format('file1.txt',100))
