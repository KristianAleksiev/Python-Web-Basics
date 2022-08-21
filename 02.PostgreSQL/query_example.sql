CREATE DATABASE my_db;
CREATE TABLE table_name;

INSERT INTO table_name VALUES ();
SELECT  * FROM table_name;
SELECT column1, column2, column3 FROM table_name;
SELECT * FROM table_name WHERE condition;


ALTER TABLE table_name DROP COLUMN column1;

ALTER TABLE table_name
ALTER COLUMN column2 VARCHAR(100);

ALTER TABLE table_name
ALTER COLUMN column3 SET DEFAULT 0;

ALTER TABLE table_name
DROP CONSTRAINT primary_key;

UPDATE table_name
SET column2=6.2
WHERE id = 1;

ORDER BY column2
THEN BY column3 DESC;4


DROP table_name;