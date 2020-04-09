import shelve
import os.path

from past.builtins import raw_input

# print("Phonebook choice:", phonebook[choice])
# print("Phonebok contacts:", phonebook['contacts'])
# print("Phonebook:", phonebook)

if not os.path.isfile('phonebook.txt'):
    phonebook = shelve.open('phonebook.txt')
    # utwórz klucz w którym będą przechowywane wartości słownika w phonebook.txt
    # tworzy słownik i jego klucze i przypisuje do tego klucza na razie pustą listę.
    phonebook['contacts'] = []
    phonebook.close()


def list_contacts():
    # otwórz książkę telefoniczną
    phonebook = shelve.open('phonebook.txt')
    # do zmiennej temp wypakuj zawartość phonebook['contacts'] - listę kontaktów
    temp = phonebook['contacts']
    # tyle razy ile jest elemetów w temp
    if temp:
        for i in range(len(temp)):
            # wyświetl kontakty o indeksach od 0 do tylu ile jest elementów w temp
            print("Contact name: %s\n" % temp[i])
            # do zmiennej choice przypisz wybór użytkownika, będzie to klucz w słowniku
            choice = raw_input("What to open: ")
            # do zmiennej contact data wypakuj kontakt (słownik) z listy kontaktów o nazwie jaka była przekazana
            # przez użytkownika
            if choice in phonebook:
                contact_data = phonebook[choice]
                # wyświetla poszczególnie zawartość słownika dla kontaktu
                print("\n")
                #                 wywołanie:  słownik['klucz'] - wyświetli "Name: wartość"
                print("Name: %s" % contact_data['1'])
                print("Surname: %s" % contact_data['2'])
                print("Phone: %s" % contact_data['3'])
                print("\n")
            else:
                print("No contact in phonebook")
                print("\n")
    else:
        print("There are no contacts in phonebook yet.")
        print("\n")
        pass


def add_contact():
    # tymczasowa pusta lista
    temp = []
    # przypisz do zmiennej otwarcie pliku phonebook.txt przez moduł shelve
    phonebook = shelve.open('phonebook.txt')
    # do tymczasowej pustej listy przypisz klucze w shelve
    # włóż do tmp to co jest w phonebook['entry']
    temp = phonebook['contacts']
    # dodaj do tmp to co wpisze użytkownik - nazwę kontaktu,
    temp.append(raw_input("Contact name: "))
    # klucz w słowniku będzie miał nazwę aktualnie przechowywaną w tmp
    # teraz dodaj to co jest w tmp spowrotem wsadź do phonebook['entry'], czyli powiększ phonebook entry o
    # kolejny element
    phonebook['contacts'] = temp
    phonebook.close()


def save_contact():
    phonebook = shelve.open('phonebook.txt')
    # dla każdego elementu w przedziale ilości elementów phonebook[entry]
    # for i in range(len(phonebook['contacts'])):
    # do zmienej tmp wsadź to co jest w phonebook['entry'] - lista kluczy
    temp = phonebook['contacts']
    # nowy słownik "x"
    contact_data = {}
    # w nowym słowniku przypisz do kluczy x['1'],x['2'] wartości.
    # będzie tak x['1'] Janusz | {1 : "Janusz"}
    contact_data['1'] = raw_input("Name: ")
    contact_data['2'] = raw_input("Surname: ")
    contact_data['3'] = raw_input("Phone: ")
    print("\n")
    # do phonebooka o kluczu z ostatniej pozycji tmp, czyli ostatniej dodanej osoby przypisz słownik x
    phonebook[temp[-1]] = contact_data
    phonebook.close()


def search_contacts():
    # otwórz książkę telefoniczną
    phonebook = shelve.open('phonebook.txt')
    # do zmiennej temp wypakuj zawartość phonebook['contacts']
    temp = phonebook['contacts']

    # print("temp:", temp)
    # temp: ['Janusz Cebula', 'jja', 'sdgsf'
    # temp[0]: ['Janusz Cebula']

    # zmienna przechowująca dane od użytkownika czego chce szukać
    search_choice = raw_input("What do you want to search for?: ")
    print("\n")
    # tyle razy ile jest elemetów w temp
    for i in range(len(temp)):
        # do zmiennej contact_data przypisz kontakt, i wskazuje na indeks kontaktu.
        contact_data = phonebook[temp[i]]  # = phonebook['Janusz Cebula']

        # print("Contact_data", contact_data)
        # Contact_data
        # {'1': 'Janusz', '2': 'Cebula', '3': 'Sosnowiec', '4': 'asas', '5': 'asasa', '6': 'asa', '7': 'a', '8': 'asa',
        # '9': 'as'}

        if search_choice in contact_data.values():
            print("Found: \n")
            print("Name: %s" % contact_data['1'])
            print("Surname: %s" % contact_data['2'])
            print("Phone: %s" % contact_data['3'])
        else:
            print("No such information")
            print("\n")
            break


def edit_contacts():
    phonebook = shelve.open('phonebook.txt')
    # wyładuj do zmiennej listę kontaktów
    temp = phonebook['contacts']
    # wyświetl kontakty
    print(temp)
    print("\n")
    # zmienna zabezpieczająca, na razie pusta lista
    backup = []
    # do zmiennej pobierz to co wpisał użytkownik
    edit_choice = raw_input("Which contact you want to edit: ")
    print("\n")
    # jeżeli to co wpisał użytkownik jest w książce
    if edit_choice in phonebook:
        # do zmiennej contact_data zaladuj słownik kontaktu tj. słownik przypisany do np Janusza Cebuli
        contact_data = phonebook[edit_choice]
        # wyświetl dane kontaktu
        print("Contact data: \n")
        # wyświetla poszczególne dane kontaktu, którego dotyczy zmiana
        print("1.Name: %s" % contact_data['1'])
        print("2.Surname: %s" % contact_data['2'])
        print("3.Phone: %s" % contact_data['3'])
        print("\n")
        # zmienna przechowująca wybór użytkownika, dot którą informację chce zmienić
        inf_choice = int(raw_input("Which information you want to change?: "))
        # do numerów przypisane są intrukcje
        if inf_choice == 1:
            # jeżeli użytkownik wybrał 1, do contact_data, w pierwszym miejscu zmień na to co wpisze użytkownik
            contact_data['1'] = raw_input("New name: ")
        elif inf_choice == 2:
            contact_data['2'] = raw_input("New surname: ")
        elif inf_choice == 3:
            contact_data['3'] = raw_input("New phone: ")
            # jeżeli wpisze coś innego
        else:
            print
            "There is no such information. "
        # zmiennej zapasowej (pustej listy) wstaw słownik (NOWE dane) wybranego kontaktu
        backup = contact_data
        # usuń z książki (listy kontaktów) element (użytkownika), którego dotyczyła edycja
        del (phonebook[edit_choice])
        # w ten sam element wpisz zawartość zmiennej (nowy słownik - nowe dane)
        phonebook[edit_choice] = backup
        # jeżeli to co wpisał użytkownik nie jest takie samo jak nazwa kontaktu
    else:
        print
        "No such contact "


def delete_contacts():
    phonebook = shelve.open('phonebook.txt')
    # wyładuj do zmiennej listę kontaktów
    temp = phonebook['contacts']
    print(temp)
    # wyświetl listę kontaktów
    print("\n")
    # do zmiennej zapasowej załaduj zawartość temp (listę kontaktów)
    delete_bckp = temp
    # do zmiennej przypisz co użytkownik chce usunąć
    delete_choice = raw_input("Which contact you want to delete?: ")
    # jeżeli wartość którą wpisał użytkownik znajduje się w książce kontaktów to
    if delete_choice in phonebook:
        # usuń z książki (listy) element podany przez użytkownika
        del (phonebook[delete_choice])
        # ze zmiennej zapasowej usuń to co podał użytkownik
        delete_bckp.remove(delete_choice)
        # do książki kontaktów załaduj nową książkę bez usuniętego elementu
        phonebook['contacts'] = delete_bckp
        # wyświetl usunięty kontakt
        print("Deleted contact: %s" % delete_choice)
        # jeżeli wartość którą użytkownik wpisał nie znajduje się w książce kontaktów
    else:
        print("There is no such contact!")


def menu():
    while True:
        choice = int(input("What do you want to do? Type a number: \n1. Contacts\n2. New contact\n3. Search"
                           "\n4. Edit contact\n5. Delete contact\n6. Quit\n"))
        if choice == 1:
            list_contacts()
        elif choice == 2:
            add_contact(), save_contact()
        elif choice == 3:
            search_contacts()
        elif choice == 4:
            edit_contacts()
        elif choice == 5:
            delete_contacts()
        elif choice == 6:
            break
        else:
            print("Please type number from 1 to 6, try again")


menu()
