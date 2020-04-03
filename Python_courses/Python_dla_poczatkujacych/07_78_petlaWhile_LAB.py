##firstRow = 1
##lastRow = 31
##currentRow = firstRow
##
##while currentRow <= lastRow:
##    print("Row number ",currentRow)
##    currentRow+=1

##i=1
##
##while i<=13:
##    print("i^2 = ",i**2,"i^3 = ",i**3)
##    i+=1


##i=1
##
##while i<=16:
##    print("2^",i," = ",2**i,sep="")
##    i+=1

##i=1
##
##while i<=10:
##    print(i*'x')
##    i+=1
    
y = 1
ymax = 13
text = '{0:d} do kwadratu to {1:d} \t {0:d} do sześcianu to {2:d}'
 
while y<=ymax:
    print(text.format(y,y**2,y**3))
    y+=1
 
print('---------------------------------')
 
a = 0
amax = 16
text2 = '{0:d} do kwadratu to {1:d}'
 
while a<=amax:
    print(text2.format(a,a**2))
    a+=1
