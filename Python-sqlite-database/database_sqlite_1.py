
import sqlite3
from employee import Employee

'''
# print(emp_1.email)

# c.execute("INSERT INTO employees VALUES('ko', 'ko', 9000)")
# c.execute("INSERT INTO employees VALUES('{}', '{}', '{}')".format(emp_1.first, emp_1.last, emp_1.pay))
# c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# c.execute("INSERT INTO employees VALUES (:first, :last , :pay)", {'first': emp_1.first, 'last':emp_1.last, 'pay':emp_1.pay})

# c.execute("SELECT * FROM employees WHERE last='ko'")
# c.execute("SELECT * FROM employees WHERE last=?", ('ko',))
# c.execute("SELECT * FROM employees WHERE last=:last", {'last':'koko'})


# print (c.fetchone())
# print(c.fetchall())

'''


conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
				first text,
				last text,
				pay integer
		)""")

def insert_emp(emp):
	with conn:
		c.execute("INSERT INTO employees VALUES (:first, :last , :pay)", {'first': emp.first, 'last':emp.last, 'pay':emp.pay})


def get_emps_by_name(first_name):
	c.execute("SELECT * FROM employees WHERE first=:first", {'first': first_name})
	return c.fetchall()


def update_pay(emp, pay):
	with conn:
		c.execute("""UPDATE employees SET pay= :pay WHERE first= :first AND last= :last""", 
			{'first': emp.first, 'last': emp.last, 'pay':pay})

def remove_emp(emp):
	with conn:
		c.execute("""DELETE from employees WHERE first= :first AND last= :last""", 
			{'first': emp.first, 'last': emp.last, 'pay':emp.pay})




emp_1 = Employee('mg', 'ko', 909899)
emp_2 = Employee('mg', 'chit', 909899)
emp_3 = Employee('mg', 'zaw', 909899)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)

data = get_emps_by_name('mg')
print (data)


update_pay(emp_2, 50000) # Update Pay
remove_emp(emp_3)


data = get_emps_by_name('mg')
print (data)


conn.commit()
conn.close()


