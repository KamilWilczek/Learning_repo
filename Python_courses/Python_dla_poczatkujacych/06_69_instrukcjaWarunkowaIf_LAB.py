##min_likes = 500
##min_shares = 100
##
##num_likes = 501
##num_shares = 100
##
##if min_likes <= num_likes and min_shares <= num_shares:
##    print("Ceny idą w dół o 10%")
##else:
##    print("Za mało lików i szerów")

##isPizzaOrdered = True
##isBigDrinkOrdered = False
##isWeekend = False
##
##if isPizzaOrdered or isBigDrinkOrdered and not isWeekend:
##    print("Za zakupy otrzymujesz kupon na burgera!")
##else:
##    print('Kupuj dalej ;)')


diskSize = 140
diskSizeUsed = 120
fileSize = 5

if diskSize > diskSizeUsed and fileSize > 0 and fileSize <= diskSize-diskSizeUsed:
    print("file can be downloaded")
else:
    print("brak miejsca na dysku")
