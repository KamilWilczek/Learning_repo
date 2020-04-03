s="A Python script"
#  A   P y t h o n   s c  r  i  p  t
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
print(s[0])
#A
print(s[2])
#P
print(s[2:7]) #od drugiego znaku do siódmego wyłącznie
#Pytho
print(s[2:8]) #od 2. znaku do 8. wyłącznie
#Python

print(s[:8]) #do 8. znaku WYŁĄCZNIE
#A Python
print(s[8:]) #od 8. znaku WŁĄCZNIE
# script

print(s[2:999])
print(s[222:999])

message = 'Document "cv.doc" was printed on printer: XEROX'
#jak w napisie znalezc nazwe drukarki
print(message.find(':'))
print(message[message.find(':'):])
print(message[message.find(':')+2:])

#jak w napisie znalezc nazwe dokumentu
print(message[message.find('"')+1:])
tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])
