import sqlite3
from employee import Employee

# database connection
conn = sqlite3.connect(':memory:')

# cursor
c = conn.cursor()

# create table
c.execute("""CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay})

def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                    {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last", 
                    {'first':emp.first, 'last':emp.last})

# creating new instances
emp1 = Employee('Jonas', 'Joe', '4000')
emp2 = Employee('Tom', 'Joe', '7000')

# run functions
insert_emp(emp1)
insert_emp(emp2)

emps = get_emp_by_name('Joe')
print(emps)

update_pay(emp2, 1000000)
remove_emp(emp1)

emps = get_emp_by_name('Joe')
print(emps)

# closing conn to db
conn.close()
