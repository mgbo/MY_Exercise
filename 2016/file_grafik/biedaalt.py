b=[]
f=open('bet8_1.log','r')

for line in f:
	a=map(int,line.split())
	print a
	if not a:
		break
	t1=a[1]
	b.append(t1)
print b
print '..........'	
clients = [1,2,3,4,1,2,1,3,2,4] # this is example data, use instead it real data got at the previous steps
client_frequency = dict() # this dictionary contains client ID as a key, and the frequency as a value

for client in clients:
    if client not in client_frequency:
        client_frequency[client] = 0
    client_frequency[client] += 1
client_with_min_freq = min(client_frequency, key = client_frequency.get)
print client_with_min_freq
