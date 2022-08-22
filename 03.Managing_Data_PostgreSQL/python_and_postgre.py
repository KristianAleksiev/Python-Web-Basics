import psycopg2
"""Data extraction from database through python"""

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

cursor = connection.cursor()

cursor.execute('SELECT * FROM employees')

# cursor.execute("UPDATE employees SET salary = 1300 WHERE job_title='System admin'")
# cursor.execute("UPDATE employees SET salary = 1500 WHERE job_title='Front-end dev'")
# cursor.execute("UPDATE employees SET salary = 2600 WHERE job_title='sr. Back-end dev'")
# cursor.execute("UPDATE employees SET salary = 5000 WHERE job_title='Manager'")
# connection.commit()


for row in cursor.fetchall():
    print(row)

connection.close()

# DJANGO ORM - Object-Relational-Mapping - Mapping Classes to Tables

# class Employee:
#     def __int__(self, name, salary, job_title):
#         self.name = name
#         self.salary = salary
#         self.job_title = job_title
#
#     def __repr__(self):
#         return f"{self.name}, {self.job_title}"
#
#
# employees = [Employee(*row) for row in cursor.fetchall()]
