
file_path = r'd:\\Python_Kursy\\Python_Udemy\\data_input\\orders.csv'

with open(file_path,'r') as file:
    for line in file:
        order = line.replace('\n','').split(',')
        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' % (order[0],order[1],order[2]))
        else:
            print("Line %s malformed!!!" % (line))
    print('End of list')
