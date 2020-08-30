
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'выходный'
        return 'Рабочий день'


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print (Employee.raise_amt) # 1.04
print (emp_1.raise_amt) #1.04
print (emp_2.raise_amt) # 1.04

print (emp_1.pay) #50000
emp_1.apply_raise() #50000 * 1.04
print (emp_1.pay) # 52000

Employee.set_raise_amt(4)

print (emp_1.raise_amt) # 4 

print (emp_2.pay) #60000
emp_2.apply_raise()
print(emp_2.pay) # 60000 * 4

emp_1.apply_raise()
print (emp_1.pay) # 52000 * 4

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# _______ обычный метод _____________
first, last, pay = emp_str_1.split('-') 
new_emp_1 = Employee(first, last, pay)
print (new_emp_1.email)
print (new_emp_1.pay)

# ________ используется метод класса (from_string) _______
new_emp_2 = Employee.from_string(emp_str_2)
print (new_emp_2.email)
print (new_emp_2.pay)


import datetime
my_date = datetime.date(2017, 11, 25)

print(emp_2.is_workday(my_date))

my_date = datetime.date(2017, 11, 27)
print (emp_1.is_workday(my_date))






