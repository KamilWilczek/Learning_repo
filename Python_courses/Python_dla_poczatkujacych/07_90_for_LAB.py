data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for tekst in data:
    tekst = tekst.upper()
    print(tekst)
else:
    print('-- end of the list --')

for tekst in data:
    elements = tekst.split(':')
    print(elements[0].upper())
    print(elements[1])
else:
    print('-- end of the list --')

for tekst in data:
    elements = tekst.split(':')
    if elements[0] == "Error":
        print(elements[1].upper())
    else:
        print(elements[1])
else:
    print('-- end of the list --')

##elements = 'Error:File cannot be open'.split(':')
##print(elements)
##print(not elements[0].find('Error'))
##print(elements[0] == 'Error')
##print(elements[0].find('Error'))
##print(elements[0] == 'Error')
##elements = 'Warning:Internet connection lost'.split(':')
##print(elements)
##print(not elements[0].find('Error'))
##print(elements[0] == 'Error')
##print(elements[0].find('Error'))
##print(elements[0] == 'Error')
