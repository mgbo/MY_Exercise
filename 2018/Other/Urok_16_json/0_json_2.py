

import json
from decimal import Decimal

# d = {}
# d['name'] = 'Luke'
# d["Country"] = 'Candda'

# print (json.dumps(d, ensure_ascii=False)) # {"name": "Luke", "Country": "Candda"}

# print (d)

#------------------------------------------------------------------
# строка которую будем парсить
json_string = """ {

  "orderID": 42,
  "customerName": "John Smith",
  "customerPhoneN": "555-1234",
  "orderContents": [
    {
      "productID": 23,
      "productName": "keyboard",
      "quantity": 1
    },
    {
      "productID": 13,
      "productName": "mouse",
      "quantity": 1
    }
  ],
  "orderCompleted": true

} """
 
# распарсенная строка
parsed_string = json.loads(json_string)

print (parsed_string) # сама переменная


print (parsed_string['customerName']) # имя покупателя

print (parsed_string["orderContents"]) # содержимое заказа

print ('-'*30)
print (parsed_string["orderContents"][0]) # отдельный пункт заказ
# {'productID': 23, 'productName': 'keyboard', 'quantity': 1}

print (parsed_string["orderContents"][0]['productName']) # товар в пункте заказа

print (parsed_string["orderCompleted"]) # Закат выполен




