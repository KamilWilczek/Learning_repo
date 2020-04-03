import os


while not fileIsOk:
    filename = input("Enter path to results file: ")

    if os.path.isfile(filename):
        break
    else:
        print('File name is not correct, try again!')

print("The reulsts file is %s" % (filename))
