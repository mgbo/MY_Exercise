
cities = ["Moscow", "Kiev", "Washington"]
states = ["Russia", "Ukraine", "USA"]
capitalsOfState = {state: city for city, state in zip(cities,states)}

print (capitalsOfState)

print ("\n-----------\n")
for k,v in capitalsOfState.items():
	print (k,v)
	
print ("\n-----------\n")

StateByC = {capitalsOfState[state]:state for state in capitalsOfState}
print (StateByC)
