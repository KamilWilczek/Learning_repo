print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

IsWeekend = True
print("Is weekend = ",IsWeekend)

Temperature = 22
print("Temperature =",Temperature)

ToDoList = ''
print("ToDoList = ",ToDoList)
# == is equal
#> greater than
#>= greater or equal
#!= npt equal
IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''
# is Happy when jest weekend, temp jest wyzsza lub rowna 20 i nie ma nic do zrobienia
print("IsHappy=",IsHappy)

print("######################################################################")
##############################################################################

IsWeekend = True
print("Is weekend = ",IsWeekend)

Temperature = 5
print("Temperature =",Temperature)

ToDoList = ''
print("ToDoList = ",ToDoList)
# == is equal
#> greater than
#>= greater or equal
#!= npt equal
IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''
print("IsHappy=",IsHappy) #jest false bo temp nie spelnia warunku >=20

print("######################################################################")
############################################################################

IsWeekend = False
print("Is weekend = ",IsWeekend)

Temperature = 5
print("Temperature =",Temperature)

ToDoList = 'Shopping'
print("ToDoList = ",ToDoList)
# == is equal
#> greater than
#>= greater or equal
#!= npt equal
IsHappy = not IsWeekend and Temperature < 20 and ToDoList != ''
#warunek bedzie spelniony jezeli weekend bedzie false, temp ponizej 20 oraz lista do zrobienia nie bedzie pusta
print("IsHappy=",IsHappy)

print("######################################################################")
############################################################################
IsWeekend = True
print("Is weekend = ",IsWeekend)

Temperature = 25
print("Temperature =",Temperature)

ToDoList = ''
print("ToDoList = ",ToDoList)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == '' \
          or not IsWeekend and Temperature < 20 and ToDoList != ''
print("IsHappy=",IsHappy)


IsHappy = IsWeekend and  Temperature >= 20 and ToDoList == '' \
          or not IsWeekend and not Temperature >= 20 and not ToDoList == ''
print("IsHappy=",IsHappy)

IsHappy = IsWeekend and  Temperature >= 20 and ToDoList == '' \
          or not IsWeekend and not (Temperature >= 20 or ToDoList == '')
print("IsHappy=",IsHappy)


