
""" JavaScript Object Notation """
import json

# people_string = '
# {
#     "people" :
#     [
#         {
#             "name": "John Smith",
#             "phone": "615-555-7164",
#             "emils": ["johnsmith@bogusemail.com", "john.smith@work-place.com"]
#             "has_license": false
#         },
#         {
#             "name": "Jane Doe",
#             "phone": "560-555-5153",
#             "emails": null,
#             "has_license": true
#         }
#     ]
# }
# '

''' convert JSON to Python object (Dict)  '''
json_data = '{"name": "Brian", "city":"seattle"}'
python_obj = json.loads(json_data)
print (python_obj)


print (python_obj["name"])
print (python_obj["city"])
print ('-'*30)

''' Convert JSON to Python Object(list)'''
array = '{"drinks":["coffee", "tea", "water"]}'
data = json.loads(array)

for element in data['drinks']:
    print (element)
print ('-'*30)

''' Convert JSON to Pyhon Object(float)'''
from decimal import Decimal


jsondata = '{"number": 1.3404830}'
x = json.loads(jsondata, parse_float = Decimal)
print (x['number'])
print ('-'*30)

''' Convert JSON to Pyhon Object (Example)'''

json_input = '{"Person":[{"name":"Brian", "city":"Seattle"},{"name":"David", "city":"Amsterdam"}]}'

try:
    decoded = json.loads(json_input)
    # Access my_data
    for x in decoded['Person']:
        print (x['name'])
except(ValueError, KeyError, TypeError):
    print ("JSON format Error")
