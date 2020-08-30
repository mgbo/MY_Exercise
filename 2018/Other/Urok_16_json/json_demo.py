
''' JavaScript Object Notation '''
import json

people_string = '''
{
    "people" : [
    {
        "name":"John Smith",
        "phone":"345-566-4544",
        "email":["johnsmith@gmail.com","johnsmith2@gmail.com"],
        "has_license": false
    },
    {
    "name":"John Doe",
    "phone":"345-566-4544",
    "email":null,
    "has_license": true
    
    }
    ]
}
'''

data = json.loads(people_string)

# print (type(data))
# print (data)

for person in data['people']:
    print (person['name'])

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)



