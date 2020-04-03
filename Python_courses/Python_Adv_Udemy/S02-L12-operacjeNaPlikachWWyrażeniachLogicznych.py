import os

path = r'/Users/kamilw/Desktop/Moje/PythonLearing/Python_Adv_Udemy/mydata.txt'

#os.remove(path)

"""
if os.path.isfile(path):
    print("File %s exists" % path)
else:
    print('Creating a file %s' % path)
    open(path,'x').close() # - 'x' - gdyyby taki plik istniał ten parametr powoduje zgłoszenie  błędu
    # zaraz po otwarciu pliku jest zamykany
    print("File %s created" % path)
"""

# result = os.path.isfile(path)
# print(result)

# result = os.path.isfile(path) or open(path, 'x').close()
# print(result)
# alternatywa jest prawdziwa gdy chociaż jeden warunek jest prawdziwy. Już pierwszy warunek jest prawdziwy więc Python
# nie sprawdza drugiego członu

result = os.path.isfile(path) and open(path, 'x').close()
print(result)
# koniunkcja jest prawdziwa tylko jeśli oba warunki są prawdziwe. Pierwsza część daje False, więc Python nie wykonuje
# drugiej części koniunkcji