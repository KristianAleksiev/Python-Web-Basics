"""
1. SQL Syntax - Case insensitive
Keywords - CAPITALS
String literals - 'x literal', enclosed in single commas
Name of columns / tables - enclosed in "" double commas
Escaping symbols - SELECT name as "City Name";

2. Data manipulation
3. Retrieving Data
4. Views - Virtual joined tables
- Query template
- Dynamic

CREATE VIEW name



5. Aggregate Functions
count(), sum(), avg(), max(), min()

SELECT count(*)
FROM employees;

6. Python and PostgreSQL
psycopg2 adapter


import psycopg2
connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)
connection.close()
"""