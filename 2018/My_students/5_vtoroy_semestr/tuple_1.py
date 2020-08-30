
"""
Особенно удобно использовать кортежи, когда необходимо возвратить из функции сразу несколько значений.
Когда функция возвращает несколько значений, фактически она возвращает в кортеж:
"""

def get_user():
    name = "Tom"
    age = 22
    is_married = False
    return name, age, is_married
 
 
user = get_user()
print(user[0])              # Tom
print(user[1])              # 22
print(user[2])              # False

(x, y, z) = (42, 13, "hike")
print (z)  ## hike
#(err_string, err_code) = Foo()  ## Foo() returns a length-2 tuple

"""
Сложные кортежи
Один кортеж может содержать другие кортежи в виде элементов. Например:
"""

countries = (
    ("Germany", 80.2, (("Berlin",3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2),("Marsel", 1.6))),
    ("Myanmar", 55, (("Yangon", 23),("mandalay", 10),("sagin", 4)))
)
 
for country in countries:
    countryName, countryPopulation, cities = country

    print("\nCountry: {}  population: {}".format(countryName, countryPopulation))

    for city in cities:
        cityName, cityPopulation = city
        print("City: {}  population: {}".format(cityName, cityPopulation))








