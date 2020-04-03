import math
degree = 360
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))

degree = 45
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
print('')

print("%d degree is %f radians" % (360, math.radians(360)))
print("%d degree is %f radians" % (45, math.radians(45)))
print('')

small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38

small_pizza_price = 11.5
big_pizza_price = 15.6
family_pizza_price = 22

small_area = math.pi * small_pizza_r**2
big_area = math.pi * big_pizza_r**2
family_area = math.pi * family_pizza_r**2

print('small', small_pizza_r,small_pizza_price, small_area)
print('big', big_pizza_r,big_pizza_price, big_area)
print('family', family_pizza_r,family_pizza_price, family_area)

print('small', small_pizza_price/small_area)
print('big', big_pizza_price/big_area)
print('family', family_pizza_price/family_area)

math_ls = dir(math)
print(math_ls)
