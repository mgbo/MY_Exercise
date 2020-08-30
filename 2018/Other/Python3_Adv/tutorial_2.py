
from string import Template

class MyTemplate(Template):
	delimeter = '#'

def Main():
	cart = []
	cart.append(dict(items="Coke", price=8, qty=2))
	cart.append(dict(items="Cake", price=13, qty=12))
	cart.append(dict(items="fish", price=30, qty=15))

	#print (cart)

	t = MyTemplate("$qty x $items = $price")

	total = 0

	for data in cart:
		print (t.substitute(data))
		total += data["price"]

	print ("Total : "+str(total))


if __name__ == "__main__":
	Main()
