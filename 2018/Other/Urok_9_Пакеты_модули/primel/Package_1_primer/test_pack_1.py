# Import classes from your brand new package
from Animals import Mammals
from Animals import Birds

Birds.myt()
print ('\n')

# Create an object of Mammals class & call a method of it
myMammal = Mammals.Mammal()
myMammal.printMembers()

# Create an object of Birds class & call a method of it
myBird = Birds.Bird()
myBird.printMembers()

