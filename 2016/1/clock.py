
#(h1,m1,m2) = map(int,raw_input().split()) # python 2 
h1,m1,m2 = map(int,input().split())

tm = h1*60+m1+m2

ansh = tm / 60 
ansm = tm % 60 

#print '%d %d' %(ansh,ansm) 

print ("%02d:%02d"%(ansh,ansm))
