
import sqlite3


conn = sqlite3.connect('employee.db')


c = conn.cursor()

# c.execute("""CREATE TABLE employees (
# 				first text,
# 				last text,
# 				pay integer
# 		)""")

# c.execute("INSERT INTO employees VALUES('Mg', 'ko', 9000)")

c.execute("SELECT * FROM employees WHERE last='ko'")

# print (c.fetchone())
print(c.fetchall())

conn.commit()

conn.close()


