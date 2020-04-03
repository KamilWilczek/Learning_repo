"""myvar = 'Hello Pycharm!'
myvar2 = myvar
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Is value the same?', myvar == myvar2)
print('Are the variables the same?', myvar is myvar2)
print(id(myvar), id(myvar2))
"""

myvar = 'Hello Pycharm!'
myvar2 = myvar+'!!'
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Is value the same?', myvar == myvar2)
print('Are the variables the same?', myvar is myvar2)
print(id(myvar), id(myvar2))


myvar2 = myvar2[:-2]
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Is value the same?', myvar == myvar2)
print('Are the variables the same?', myvar is myvar2)
print(id(myvar), id(myvar2))
#dwa napisy sa takie same (==) ale to sa dwa rozne obiekty w pamiecie (is)