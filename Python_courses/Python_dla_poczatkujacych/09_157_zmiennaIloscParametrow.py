def DoAction(action, parameter):
    print("action:", action)
    print("parameter:", parameter)
    return

DoAction('buy','shoes')

#DoAction('buy','shoes','socks')
# *parameter tworzy tuple
def DoAction2(action, *parameter):
    print("action:", action)
    print("parameter:", parameter)
    for element in parameter:
        print('element is',element)
    return

DoAction2('buy','shoes','socks')
DoAction2('buy','shoes','socks','t-shirt')

# **parameter tworzy słownik
def DoAction3(action, what, **parameter):
    print("action:", action)
    print("what:",what)
    print("parameter:", parameter)
    for element in parameter:
        print(element,'=',parameter[element])
    return

DoAction3('buy','shoes',size=45,color='brown',type='sport')
