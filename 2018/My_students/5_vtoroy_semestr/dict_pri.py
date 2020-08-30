"""

-------------- Комплексные словари -------------------
Кроме простейших объектов типа чисел и строк словари также могут хранить 
и более сложные объекты - те же списки, кортежи или другие словари:

"""
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}

"""
В данном случае значение каждого элемента словаря в свою очередь представляет отдельный словарь.

Для обращения к элементам вложенного словаря соответственно необходимо использовать два ключа:
"""
old_tome = users["Tom"] # {'phone': '+971478745', 'email': 'tom12@gmail.com'}
print (old_tome)

old_phone = users["Tom"]["phone"]# '+971478745'
print (old_phone)

old_email = users["Tom"]["email"] #tom12@gmail.com
print (old_email)


key = "skype"
if key in users["Tom"]:
    print(users["Tom"]["skype"])
else:
    print("skype is not found")







