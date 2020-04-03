print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
q = "THE EYES"
print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6]) #moje
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
q = "a gentleman"
print(q[3:]+q[6:]+q[7:]+q[2:]+q[0:]+q[4:]+q[5:]+q[1:]+q[8:]) #moje
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:])
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8:])
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
a = "THE MORSE CODE"
print(a[1:3]+a[6]+a[8]+a[3]+a[10:12]+a[4]+a[13]+a[9]+a[12]+a[11]+a[0]+a[7]) #moje
print(a[1:3],a[6],a[8],a[3],a[10:12],a[4],a[13],a[9],a[12],a[5],a[0],a[7])
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# 'Program "Kropka nad i" nadamy o: 22:00'

line = 'Program "Kropka nad i" nadamy o: 22:00'
print(line)


time = line[line.find(':')+2:]
print(time)

tmp = line[line.find('"')+1:]
title = tmp[:tmp.find('"')]
print(title)

print(title,time)

line2 = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
print(line2.find(':'))
time = line2[line2.find(':')+2:]
print(time)

tmp = line2[line2.find('"')+1:]
title = tmp[:tmp.find('"')]
print(title)

print(title,time)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
