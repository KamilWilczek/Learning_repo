'''
drive = 'c:\' - backslash przed ostatnim apostrofem zmienia znaczenie apostrofu
i nie jest on już apostrofem zamykajacym a po prostu apostrofem. Aby apostrof
zamienic na zamykajacy trzeba zrobic podwojny backslash
'''

drive = 'c:\\'
folder = 'scripts\\python\\'
file = 'myscripts.py'
path = drive + folder + file #konkatenacja - dodawanie napisów
print(path)
# >>>path
# w idle pokaze 'c:\\scripts\\python\\myscript.py'

justText = "text with \nnewline"
print(justText)
justText2 = r"text with \nnewline"
print(justText2)

'''
literka r pozwolila na wyswietlenie tekstu surowego "raw" i backslash nie
jest wykonywany jako znak specjalny
nie dochodzi do interpretacji znakow specjalnych
'''

justText3 = "Mc Donald's"
print(justText3)
justText4 = 'Mc Donald\'s' #jezeli nie chcesz uzywac cudzyslowu
print(justText4)
line='He said "I like Python!"'
print(line)

