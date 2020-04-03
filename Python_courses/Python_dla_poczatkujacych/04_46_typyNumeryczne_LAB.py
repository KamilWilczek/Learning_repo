name = 'Kamil'
age = 27
daysInYear = 365
daysOld = age*daysInYear

message = '%s is %d years old, so is about %d days old'

print(message % (name,age,daysOld))

name = 'Chris'
age = 17
daysInYear = 365
daysOld = age*daysInYear
print(type(daysOld))
print(type(age))
print(type(name))
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,daysOld))
a=1234567890
b=12345
dc = a // b
dm = a % b

wynik = '%d divided by %d is %d and the rest is %d'
print(wynik % (a,b,dc,dm))

wynik = '{0:d} divided by {1:d} is {2:d} and the rest is {3:d}'
print(wynik.format(a,b,dc,dm))

print('1234567890 divided by 12345 is ',1234567890 // 12345,'and the rest is',1234567890 % 12345)
