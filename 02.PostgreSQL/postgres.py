"""
1. Data management
- Faster work than just files, optimized
- Control over the data
- Tools to manipulate and manage data in a database

2. Database engine
- Clients - Engine - Database, response - Managing queries
- Each row is called a record - Class instance
- Each column is called a field - Instance property

3. Table relations
- Primary key / Foreign key interconnections
- Normalized model as a goal for data organization most of the time
- Primary key - Unique for each table - ID
- Foreign key - Points to a location where the information is stored
- Avoiding repeating data

Relationships types:
- One to One - (person - phone) - Django Auth system
- One to Many - (country - cities) - Most used relationship type
- Many to Many - (employees - projects) - Mapping table included as mediating instrument, primary keys relationships

4. Structured Query Language
- Managing data in a relational database, communicates with the Engine
- Pretty universal, same core, different engines

Language elements:
- Queries - 1 or more statements
- Clauses
- Expressions
- Predicates
- Statements

Four logical divisions:
- Data Definition - Data structure description
CREATE, ALTER, DROP

- Data Manipulation - store and retrieve, CRUDs
SELECT, INSERT, UPDATE, DELETE

- Data Control - Permissions
GRANT, REVOKE, DENY

- Transaction Control - Bundle operations - order of execution
COMMIT, ROLLBACK, SAVE

5. PostgreSQL
- Object - Relational Database Management System
- Open source
- Active community
- Very fast

cat docker-compose.yml
docker-compose up -d

6. Data types in PSQL

7. Basic SQL commands
- id SERIAL PRIMARY KEY -> Primary key
- column_name REFERENCES -> Parent table
- email VARCHAR(50) UNIQUE -> Unique constraint
- ALTER TABLE
"""
