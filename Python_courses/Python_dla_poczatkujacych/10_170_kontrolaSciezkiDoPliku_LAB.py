import os
import datetime
# d:\Python_Kursy\Python_Udemy\data_input
input_path = r'd:\Python_Kursy\Python_Udemy\data_input'

output_path = r'd:\Python_Kursy\Python_Udemy\data_output'

today = datetime.date.today()
today_output_catalog = os.path.join(output_path,today.strftime("%Y-%m-%d"))

#checking conflicts
 
#input folder must exist
is_input_catalog_ok = os.path.isdir(input_path)

#output folder must exist
is_output_catalog_ok = os.path.isdir(output_path)

#today output catalog cannot exist
is_today_output_catalog_ok = not (os.path.isdir(today_output_catalog)) and not(os.path.isfile(today_output_catalog))

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')

else:
    print("Prerequisities not met! Check tha paths!")

    #display detailed error conditions
    if not is_input_catalog_ok:
        print('Input catalog %s must exist!' % input_path)
    if not is_output_catalog_ok:
        print('Output catalog %s must exist!' % output_path)
    if not is_today_output_catalog_ok:
        print("Today's output %s cannot exist (neither as file nor as directory)!" % today_output_catalog)

    




