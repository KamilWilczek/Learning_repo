atext="This is a text."
atext.endswith('ext')
atext.endswith('ext.')
atext.islower()
atext.upper()
atext.isupper()
atext.upper().isupper()
atext.find('is')
atext.find('is',3)
##atext.replace('a',4)
##replace() argument 2 must be str, not int
atext.replace('a',"4")
atext.replace('a',"4").replace('i','1').replace('e','3')
##>>> atext.replace('a',"4").replace('i','1').replace('e','3')
##'Th1s 1s 4 t3xt.'
##>>> atext.split(' ')
##['This', 'is', 'a', 'text.']
##>>> somethingLikeNumber='1000'
##>>> somethingLikeNumber+1
##Traceback (most recent call last):
##  File "<pyshell#14>", line 1, in <module>
##    somethingLikeNumber+1
##TypeError: can only concatenate str (not "int") to str
##>>> somethingLikeNumber.isdigit()
##True
##>>> somethingLikeNumber.isdecimal()
##True
##>>> somethingLikeNumber.isalpha()
##False
##>>> somethingLikeNumber.isalnum()
##True
##>>> 
