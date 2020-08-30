

my_dict = {'a': 1, 'c': 3, 'e': 5, 'f': 6, 'b': 2, 'd': 4}

mysorted = sorted(my_dict)
print(mysorted)           # ['a', 'b', 'c', 'd', 'e', 'f']

mysorted = sorted(my_dict.items())
print(mysorted)           # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]

mysorted = sorted(my_dict.values())
print(mysorted)           # [1, 2, 3, 4, 5, 6]


population = {
"Shanghai": 24256800,
"Karachi": 23500000,
"Beijing": 21516000,
"Delhi": 16787941
}


# отсортируем по возрастанию населения:
population_sorted = sorted(population.items(), key=lambda x: x[1]) # sort by values

print(population_sorted)
# [('Delhi', 16787941), ('Beijing', 21516000), ('Karachi', 23500000), ('Shanghai', 24256800)]

population_sorted_1 = sorted(population.items(), key=lambda x: x[0]) # sort by key
print (population_sorted_1)


