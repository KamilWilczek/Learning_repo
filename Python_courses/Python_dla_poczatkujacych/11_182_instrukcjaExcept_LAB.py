import sys

file_path = r'd:\Python_Kursy\Python_Udemy\data_input\orders.csv'
    
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
        try:
            
 
        # ADD YOUR CODE HERE
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' \
                  % (pharmacy_name, item, amount))
        except ValueError as e:
            print('Error due to incorrect data conversion in the third field to type int. Line: %s"' % line)
        except IndexError as e:
            print('Error related to the lack of sufficient fields: ', line)
            
        except:
            print("Problem with line %s" % line, sys.exc_info()[0])
 
print("Processing finished")
