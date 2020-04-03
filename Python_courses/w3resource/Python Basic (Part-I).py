# """
# 1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
#
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are
# """
# print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike "
#       "a diamond in the sky\n"
#       "Twinkle, twinkle, little star,\n\tHow I wonder what you are")
#
# print("\n----------------------------------------------\n")
# """
# 2. Write a Python program to get the Python version you are using.
# """
#
# import sys
# print("Python version: ", sys.version)
# print("Version info: ", sys.version_info)
#
# print("\n----------------------------------------------\n")
# """
# 3. Write a Python program to display the current date and time.
# """
#
#
# from datetime import datetime
# print("Current date and time is: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
# print("\n----------------------------------------------\n")
# """
# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
# """
# from math import pi
# r = float(input("Please type the radius of the circle: "))
# Area = pi * r**2
# print(" Area of the circle with radius %2f is %f: " % (r,Area))

#print("\n----------------------------------------------\n")
# """
# 5. Write a Python program which accepts the user's first and last name and print them in reverse order
#  with a space between them.
# """
#
# user = input("Please enter your name and last name: ")
# list = user.split()
# print(list[1] + ' ' + list[0])

#print("\n----------------------------------------------\n")
# """
# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and
# generate a list and a tuple with those numbers.
# """
#
# numbers = input("Plese type sequence of numbers: ")
# list = numbers.split(',')
# tuple = tuple(list)
# print(list,tuple)

# print("\n----------------------------------------------\n")
# """
# 7. Write a Python program to accept a filename from the user and print the extension of that.
# """
#
# name = input("Please type program name with extension: ")
# list = name.split('.')
# print('Extension is: ', repr(list[1]))

# print("\n----------------------------------------------\n")
# """
# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# """
#
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])

# """
# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# """
# exam_st_date = (11, 12, 2014)
# print("The examination will start from: %i / %i / %i" % exam_st_date)

# """
# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# """
#
# n = int(input("Input an integer: "))
# n1 = int("%s" % n)
# n2 = int("%s%s" % (n,n))
# n3 = int("%s%s%s" % (n,n,n))
# print(n1+n2+n3)

# """
# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
# """
# print(print.__doc__)

# """
# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
# """
#
# import calendar
# yr = int(input("For what year you want me to show calendar? "))
# mth = int(input('For what month? '))
# print(calendar.month(yr,mth))

# """
# 13. Write a Python program to print the following here document.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """
#
# print("""
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """)

# """
# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
# """
#
# import datetime
# date1 = datetime.date(2014, 7, 11)
# date2 = datetime.date(2014, 7, 2)
# delta = date1 - date2
# print(delta.days)

"""
15. Write a Python program to get the volume of a sphere with radius 6.
"""
from math import pi
r = 6
Vol = 4/3*pi*r**3
print("Volume of the sphere with radius 6 is: ", Vol)
