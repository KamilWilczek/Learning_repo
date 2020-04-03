print('######################################################')

isAutomaticMode = False
'''
zmienna logiczna, o następującym znaczeniu: wartość True oznacza, że kierowca
ustawił pokrętło sterujące światłem na tryb automatyczny. Sterownik ma
podejmować decyzję o zapaleniu świateł tylko jeżeli wartość tej zmiennej to
True, ale zapalenie świateł zależy jeszcze od kolejnych warunków.
'''

is80PercentLight = True # is the level of day-lighr above 80%
'''
True oznacza, że "chyba" mamy dzień, bo jest dość dużo światła. Światła w
samochodzie powinny być zgaszone o ile nie ma innych warunków, które wpływałyby
na to, że światła mają się świecić. Jeśli wartość zmiennej to False, tzn. że
jest dość ciemno i światła powinny się zaświecić, oczywiście o ile jesteśmy w
trybie automatycznym
'''
isDirectLight = False # is the Sun ligthing directly into the driver's face
'''
zmienna logiczna o następującym znaczeniu: wartość True oznacza, że nisko
położone słońce świeci wprost w oczy kierowcy. Wprawdzie ciemno nie jest,
ale w takich warunkach światła powinny się zaświecić, oczywiście jeśli jesteśmy
w trybie automatycznym.
'''
isRainy = True # is it rainy, foggy or other weather conditions are present
'''
zmienna logiczna o następującym znaczeniu: wartość True oznacza,
że pada deszcz, jest mgła lub mamy do czynienia z innymi niekorzystnymi
warunkami atmosferycznymi. O ile jesteśmy w trybie automatycznym, to należy
zaświecić światła.
'''
turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight \
                                    or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
