

cites = ["NayPyiTaw","Moscow","Kuev","Washington"]
states = ["Myanmar","russia","Ukaine","USA"]

# создаем dit (capital_st)
capital_st = {sta:cit for cit,sta in zip(states,cites)}
print (capital_st)

D = zip(states,cites)
print (D)
for k,v in D:
	print (k,v)
	
#value=capital_st['mm'] #не будет работь потому что ключа нет в словаре
#print (value)

A_pop = capital_st.pop('mmmm',5)
print (A_pop)

value = capital_st['NayPyiTaw']
print (value)

value_1 = capital_st.get('mm')
print (value_1)

value_2 = capital_st.get('mm',1)
print (value_2)

print (capital_st)


