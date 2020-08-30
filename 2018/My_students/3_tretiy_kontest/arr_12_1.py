
dengi = int(input())

def bankomat(dengi):
	pyat_tysyachi = dengi//5000
	dengi = dengi%5000

	tysyache = dengi/1000
	dengi = dengi%1000

	pyat_sot = dengi//500
	dengi = dengi%500

	sto = dengi//100
	dengi = dengi%100

	pyat_desyat = dengi//50
	dengi = dengi%50

	desyat = dengi//10
	dengi = dengi%10

	pyat = dengi//5
	dengi = dengi%5

	dva = dengi//2
	dengi = dengi%2

	odin = dengi//1
	
	return pyat_tysyachi,tysyache


print (bankomat(dengi))
'''

print ("5000 %d"%pyat_tysyachi)
print ("1000 %d"%tysyache)
print ("500 %d"%pyat_sot)
print ("100 %d"%sto)
print ("50 %d"%pyat_desyat)
print ("10 %d"%desyat)
print ("5 %d"%pyat)
print ("2 %d"%dva)
print ("1 %d"%odin)
'''
