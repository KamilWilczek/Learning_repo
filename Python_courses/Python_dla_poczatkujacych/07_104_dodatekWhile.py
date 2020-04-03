##initialCapial = 20000
##percent = 0.03
##maxTimeYears = 10
##year = 0
##savings = 20000
##
##while year <= maxTimeYears:
##    money = savings * percent
##    savings = round(savings + money,2)
##    #savings = round((1+percent)*savings,2)
##    year += 1
##    print("Oszczędności wynoszą: ",savings)
##else:
##    print("Oszczędzone pieniądze po 10 latach: ", round(savings-initialCapial,2))

##number = 20730906
##tmp = number
##sumOfDigits = 0
##
##while tmp >0:
##    digit = tmp % 10
##    sumOfDigits += digit
##    tmp = tmp//10
##    print(digit,sumOfDigits,tmp)
##else:
##    print('The sum of digits of ', number, ' is', sumOfDigits)

#prostszy sposób:
##number = 20730906
##
##lista = str(number)
##
##print (lista)
##
##i=0
##
##suma=0
##
##while i<len(lista):
##
##    suma = suma + int (lista[i])
##
##    i += 1
##
##print ("Suma tych cyfr (tej liczby:",number,") to: ", suma)
    
    
text = """United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier."""


shortWords = 0
longWords = 0
wordLength = 6
i = 0
marks = ['.',',',':','(',')']
n = 0
#funkcja usuwajaca znaki specjalne
for mark in marks:
    text = text.replace(marks[n],'')
    n += 1
listOfWords = text.replace('\n',' ').split(' ')
while i<len(listOfWords):
    if len(listOfWords[i]) > wordLength:
        longWords += 1
    elif len(listOfWords[i]) > 0:
        shortWords += 1
    i += 1
print("Words shorter than ", wordLength, ":", shortWords)
print("Words longer than ", wordLength, ":", longWords)
