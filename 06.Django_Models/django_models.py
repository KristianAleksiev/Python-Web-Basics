"""
1. Model benefits
- Working with data using python (ORM), focused on the data and the business logic
- Django automatically creates the needed queries and executes them

-----------------------------------------------------------------

2. ORM:
App/models:
class Employee(models.Model):
first_name = models.CharField(max_length=30)
last_name = models.CharField(max_length=40)

Mapped to =>

CREATE TABLE employees_employee(
"id" SERIAL NOT NULL PRIMARY KEY,
"first_name" VARCHAR(30) NOT NULL,
"last_name" VARCHAR(40) NOT NULL,
);

- The queries are managed, without the type of DB (SQLite, MySQL, PostgreSQL)
- The column type is different with the different type (VarChar, NVarChar).. -> Django is Predefined (CharField)

CharField - small text with one required max_length argument, (db_collation)
TextField - big text
IntegerField - integer
FloatField - not accurate
DecimalField - Fixed precision decimal number, two required params (max_digits, decimal_place)
DateField - (datetime.date) - (auto_now, auto_now_add)
TimeField - (datetime.time) - (auto_now, auto_now_add)
URLFied
EmailField

Other often-used field options:
- null - False by default -> DJANGO default="NO NAME"
- blank - False by default, the field is allowed to be blank, validation related - FORMS
- unique
- primary key could be overridden -> By default django adds it, primary_key=True in the model class


3. CHOICES: -> Comes from DJANGO, not the base
Inside models.Class
job_title = models.IntegerField(
        max_length=30,
        choices=(
            (1, "Software developer"),
            (2, "Data Scientist"),
            (3, "DevOps"),
        )
    )
On initiation, the entity's job title will have to be 1 of the three => FROM DJANGO ADMIN

DYNAMICALLY =>
    company = models.CharField(
        max_length=max(len(c) for c in [AMAZON, GOOGLE]),
        choices=(
            (AMAZON, AMAZON),
            (GOOGLE, GOOGLE),
        )
    )

-----------------------------------------------------------------

4. VERBOSE_NAME
first_name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="First name",
    )

-----------------------------------------------------------------

5. Relationships in Django Models
- ForeignKey - Requires two positional arguments
  Class, on_delete

One-To-Many:
- Defining the foreign key: =>
class Department(models.Model):
    name = models.CharField(max_length=50, )
class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


Many-To-Many:
class Employee(models.Model):
    pass

class Project(models.Model):
    employees = models.ManyToManyField(to=Employee)

ON_DELETE option:
CASCADE - when the object is deleted, Django deletes all objects containing the ForeignKey
PROTECT - Prevent deletion of the referenced object
RESTRICT - ~
DO_NOTHING

-----------------------------------------------------------------

6. Class META
- Anything that's not a "field"
- Inner class, uses meta options
- Django part of the Model

- list_display - which columns to show

    class Meta:
        ordering = ('company', '-first_name',)

ABSTRACT - Does not generate a table for it, makes the extended class abstract
class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True, <= Adds it only on creating
    )
    updated_on = models.DateTimeField(
        auto_now=True <= Updates it every time it is updated
    )
    class Meta:
        abstract=True
class Department(AuditEntity):

-----------------------------------------------------------------

7. Model methods:
- str
- get_absolute_url
def get_absolute_url(self):
    return reverse("department details: ", kwargs={
        "id": self.id
    })

-----------------------------------------------------------------

8. Generating SQL queries through views:
def list_departments(request):
    context = {
        "departments": Department.objects.all()
            }

    return render(request, "list_departments.html", context)

(Department.objects.filter(name__contains="X"))
(Department.objects.get(first_name="Pesho") <= Exception if an object is not found, Exactly 1 returned

Class.objects. => Entry point for queries to the database
Injected:
{% for department in departments %}
        <li> {{ department.name }}</li>
        {% endfor %}


Using the keys in a relationship:
<li> {{ employees.first_name }} ({{employee.department.name}})</li>

-----------------------------------------------------------------

9. Migrations
- Changes made to the models (State of the database)

- python manage.py sqlmigrate - Gets the DB query generated for the migration (Every SQL) ==>
  python manage.py sqlmigrate employees 0001_initial

python manage.py showmigrations
N.B.! Migrations are reversible

python manage.py inspectdb > db.sql => Creating models from database
"""
