

(lenn,step)=map(int,input().split())

i=0
delta_path = lenn


while delta_path >= step:
	delta_path = delta_path - step
	i=i+1

print (delta_path)
print (i)
