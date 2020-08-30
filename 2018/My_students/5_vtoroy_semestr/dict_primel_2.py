
Cities = ["Moscow", "Kiev", "Washington"]
States = ["Russia", "Ukraine", "USA"]

CapitalsOfState = {state: city for city, state in zip(Cities, States)}

for k,v in CapitalsOfState.items():
	print (k,v)

StateByCapital = {CapitalsOfState[state]: state for state in CapitalsOfState}
print (StateByCapital)


print (CapitalsOfState['Russia'])


value = CapitalsOfState['Ukraine']
print (value)




