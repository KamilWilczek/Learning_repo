##min_likes = 500
##min_shares = 100
##
##num_likes = 550
##num_shares = 101
##
##if num_likes < min_likes:
##    print("Za mało lików do promocji")
##else:
##    if num_shares < min_shares:
##        print("za mało szerów do promocji")
##    else:
##        print("Ceny idą w dół")
##        
##print('----')
##
##if num_likes < min_likes:
##    print("Za mało lików do promocji")
##elif num_shares < min_shares:
##    print("za mało szerów do promocji")
##else:
##    print("Ceny idą w dół")

##if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
##
##    print('GREAT! Today our prizes drop 10% !!!')
##
##else:
##
##    if num_likes <MIN_LIKES:
##
##        print('We still need more likes to start the promotion')
##
##    else:
##
##        print('We still need more shares to start the promotion')

##if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
##
##    print('GREAT! Today our prizes drop 10% !!!')
##
##elif num_likes <MIN_LIKES:
##
##     print('We still need more likes to start the promotion')
##
##else:
##
##     print('We still need more shares to start the promotion')

isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = False

##if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
##
##    print('Burger for FREE!!!')
##
##else:
##
##    if isWeekend:
##
##        print('Come back on non-Weekend day')
##
##    else:
##
##        print('You need to order Pizza or Big drink to have a Burger coupon')
##
##

if isPizzaOrdered or isBigDrinkOrdered and not isWeekend:
    print("Za zakupy otrzymujesz kupon na burgera!")
elif isWeekend:
    print('Promocja obowiązuje tylko w dni robocze')
else:
    print('Aby skorzystać z promocji należy zamówić pizzę lub duży napój')


##diskSize = 140
##diskSizeUsed = 120
##fileSize = 5
##
##if diskSize > diskSizeUsed and fileSize > 0 and fileSize <= diskSize-diskSizeUsed:
##    print("file can be downloaded")
##else:
##    print("brak miejsca na dysku")
