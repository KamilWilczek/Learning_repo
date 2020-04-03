print("TVP1","TVP2","TVN","Polsat","BBC","HBO","MTV")
print("TVP1","TVP2","TVN","Polsat","BBC","HBO","MTV", sep=";")
print("I like computers but better is TVP1 but better is TVP2 but \nbetter is TVN but better is Polsat but better is BBC but \nbetter is HBO but better is MTV")
print("I like computers","TVP1","TVP2","TVN","Polsat","BBC","HBO","MTV", sep=" but better is ")

ProgramName = 'BBC'
Item = "News"
Time = "18:00"

print("I like watching ",Item,"at",Time,"on",ProgramName,".") #jak zrobic zeby nie bylo spacji przed kropka?
print("I like watching ",Item," at ",Time," on ",ProgramName,".", sep="") #dodajemy spacje przed kazdym stalym tekstem bez kropki i rozdzielamy separatorem bez znaku (sep=""), (sep=" ") - to separator spacji

a= 'Napis'*10 # jak zrobic aby wyprintowalo "Napis" w nowej lini 10 razy, zle
print(a, sep="\n")
print('Napis'*10, sep="\n")
b= 'Napis\n'*10 # jak zrobic aby wyprintowalo "Napis" w nowej lini 10 razy, dobrze
print(b)
