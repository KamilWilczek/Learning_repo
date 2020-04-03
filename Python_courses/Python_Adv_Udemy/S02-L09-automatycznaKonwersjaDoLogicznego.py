#isOK = True
#print("Varaible isOK: ", isOK, type(isOK))
#if isOK:
#    print('TRUE')

#isOK = 'True'
#print("Varaible isOK: ", isOK, type(isOK))
#if isOK:
#    print('TRUE')

#isOK = 'TRUE'
#print("Varaible isOK: ", isOK, type(isOK))
#if isOK:
#    print('TRUE')

#isOK = 'OK'
#print("Varaible isOK: ", isOK, type(isOK))
#if isOK:
#    print('TRUE')

#isOK = 'PYTHON'
#print("Varaible isOK: ", isOK, type(isOK))
#if isOK:
#    print('TRUE')

#isOK = 'FALSE'
#print("Varaible isOK: ", isOK, type(isOK))
#if isOK:
#    print('TRUE')

#isOK = 'False'
#print("Varaible isOK: ", isOK, type(isOK))
#if isOK:
#    print('TRUE')

# w przypdaku napisów jeżeli jest niepusty zawsze będzie to PRAWDA, pusty to FAŁSZ
isOK = ''
print("Varaible isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

# podczas konwersji liczby na wartość logiczną Python patrzy tylko na to czy coś jest czyli "nie zero" czy nie ma "zero"
isOK = 1
print("Varaible isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = 0
print("Varaible isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = [1,2,3]
print("Varaible isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = []
print("Varaible isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = [0,0,0]
print("Varaible isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

# linijka if sie nie wykona bo zerowy element listy to zero czyli FAŁSZ
isOK = [0,0,0]
print("Varaible isOK: ", isOK, type(isOK))
if isOK[0]:
    print('TRUE')

listOfErrors = [100,101,102]
print("Variable isOK: ", listOfErrors, type(listOfErrors))
if listOfErrors:
    print('TRUE')

listOfErrors = [100,101,102]
print("Variable isOK: ", listOfErrors, type(listOfErrors))
if len(listOfErrors) > 0:
    print('TRUE')