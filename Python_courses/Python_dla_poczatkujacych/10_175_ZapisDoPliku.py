filename = 'd:\\Python_Kursy\\Python_Udemy\\output.txt'

line= 'Europe'

cities = ['London','Berlin','Paris','Warsaw','Madrid','Rome']

file = open(filename, 'w')
# w - write - kazdorazowo kasuje zawartosc pliku i wpisuje nowe
# r - read
# a - append - nie kasuje zawartosci pliku tylko dopiuje
# w+ - do zapisu i odczytu
# a+ - do odczytu i zapisu

file.write(line)
file.write("\n")
#file.writelines(cities)

for city in cities:
    file.write(city+"\n")

file.close()
