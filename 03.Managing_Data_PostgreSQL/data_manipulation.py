"""
1. Inserting data
- Existing records to create new table:

CREATE TABLE customer_contacts
AS SELECT customer_id, first_name, email, phone
FROM customers;

- Inserting into an existing table => caching

INSERT INTO projects(name, start_date)   => (list of columns)
SELECT CONCAT(name,' ', 'Restructuring'), NOW()
FROM departments;

------------------------------------------------------

2. Updating
UPDATE employees
SET last_name = 'Brown'
WHERE employee_id = 1;

UPDATE employees
SET salary = salary * 1.10,
    job_title = CONCAT('Senior', ' ', job_title)
WHERE department_id = 3;

N.B.! If keyword WHERE is left out, all rows in the table will be updated

UPDATE employees
SET salary = salary * 1.4,
    job_title = CONCAT('sr.',' ',job_title)   ('sr. ' || job_title)
WHERE job_title = 'Back-end dev'

SELECT salary
FROM employees;

------------------------------------------------------

3. Deleting
- Delete a row
DELETE FROM employees
WHERE employee_id = 1;
N.B.! Keyword WHERE!!

- Delete all rows
TRUNCATE TABLE employees;  - Faster than delete

- Delete Foreign-Key references
- No action / CASCADE

------------------------------------------------------

4. Retrieving data - Projection / Selection
- Selection
SELECT *
FROM employees
WHERE job_title = 'Back-end developer';

- Projection
SELECT name
FROM cities;

- Combined
SELECT name
FROM cities
WHERE country_id = 1;

- Combining data from different tables

SELECT *
FROM cities
JOIN countries
ON cities.country_id = countries.id;

SELECT cities.name AS 'City', countries.name AS 'Country'
FROM cities
JOIN countries
ON cities.country_id = countries.id;


CREATE TABLE cities_full
AS
SELECT cities.name AS 'City', countries.name AS 'Country'
FROM cities
JOIN countries
ON cities.country_id = countries.id;

- Combining data from same table - Need to be named
SELECT *
FROM employees e
JOIN employees m
ON e.manager_id = m.id;

"""