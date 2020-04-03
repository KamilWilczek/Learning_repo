##i = 10
##result = 1
## 
##for j in range(1,i+1):
##    result *= j
## 
##print(i, result)
## 
##print('------------')

##i = 10
##for j in range(1,i+1):
##    result=1
##    for k in range(1,j+1):
##        result *= k
##    print('Silnia ',j, '=', result)
##
##print('------------')

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(noun, adj)
