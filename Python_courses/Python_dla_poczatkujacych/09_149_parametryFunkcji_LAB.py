def PrintAnimal(animal):
    if animal == "cat":
        txt1 = r'''
|\---/|
| o_o |
 \_^_/'''
        print(txt1)
    elif animal == "bear":
        txt2 = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
        print(txt2)
    elif animal == "bat":
        txt3 = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/       '''
        print(txt3)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % (animal))
    return

PrintAnimal(animal = 'bat')

def DaysToEndOfYear(year,month,day):
    from datetime import date
    input_date = date(year,month,day)
    current_year = input_date.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - input_date
    print(delta.days)
    return

DaysToEndOfYear(2020,1,20)


