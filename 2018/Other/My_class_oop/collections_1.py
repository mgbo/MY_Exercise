
from collections import defaultdict

colours = (
	('Yasoob','Yellow'),
	('Ali','Blue'),
	('Arham','Green'),
	('Ali','Black'),
	('Yasoob','Red')
	)

favourite_colours = defaultdict(list)

for name,colour in colours:
	favourite_colours[name].append(colour)

print (favourite_colours)

