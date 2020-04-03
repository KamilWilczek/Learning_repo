import os
import time

# os.getcwd() - zwraca informację o bieżącym katalogu
print("Current directory is:", os.getcwd())

# os.path.join(x,y) - łączy ścieżki plików, w tym wypadku ścieżki dwóch zmiennych
currentDir = os.getcwd()
filename = "results.txt"
fullpath = os.path.join(currentDir,filename)
print("\nThe constructed file path is: ",fullpath)

# os.path.abspath(x) - zwraca informację o absolutnej ścieżce pliku z literą dysku
relativePath = 'output.txt'
print("\nThe absolute path is: ", os.path.abspath(relativePath))

# os.path.basename(x) - zwraca nazwę pliku ze ścieżki
#os.path.dirname(x) - zwraca katalog ze ścieżki
filepath = r'c:\temp\results.txt'
print("\nThe file name part is: ", os.path.basename(filepath))
print("The directory part is: ", os.path.dirname(filepath))

# os.path.exists(x) - sprawdza czy plik istnieje
print("\nIs file existing? ",os.path.exists(filepath))
filepath = os.path.join(currentDir,filename)
print("\nIs file existing? ",os.path.exists(filepath))

if os.path.exists(filepath):
    # os.path.getmtime(x) - czas ostatniej modyfikacji
    # os.path.getctime(x) - czas utworzenia
    # os.path.getatime(x) - czas ostatniego dostępu
    print("\nLast modify date is:",os.path.getmtime(filepath))
    print("Last modify date is:",time.localtime(os.path.getmtime(filepath)))
    # os.path.getsize(x) - zwraca wielkość pliku/folderu
    print("\nFile size is: ", os.path.getsize(filepath))

    print("\nIs it a file?", os.path.isfile(filepath))
    print("Is it a dir? ", os.path.isdir(filepath))

    print("\nPath splitted:", os.path.split(filepath))
    print("Only file name part:", os.path.split(filepath)[1])

    print("\nPath splitted into drive:", os.path.splitdrive(filepath))
    print("Only drive:", os.path.splitdrive(filepath)[0])

    
