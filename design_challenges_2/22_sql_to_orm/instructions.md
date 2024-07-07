## Convert SQL queries to ORM

SQL queries and SQLAlchemy ORM queries are two ways of querying relational databases, but they differ in their syntax 
and approach. 

SQL queries involve writing SQL statements directly in the code to retrieve data from the database. On the other hand, 
SQLAlchemy ORM queries are written in Python and use an object-oriented approach to interact with the database. 
Rather than writing SQL statements, developers define classes and their attributes that map to database tables and 
columns. These classes are known as ORM models, and they provide an abstraction layer between the application code 
and the database.

In summary, while SQL queries require knowledge of SQL syntax and are more focused on the database structure, 
SQLAlchemy ORM queries provide a higher level of abstraction and can make database interactions more intuitive and 
Pythonic.



## Challenge

For this challenge you need to convert the SQL queries / syntax in the event api application to ORM. At the end of the 
conversion, there should be no SQL code directly written as string inside the code of the api application. You also need 
to create the database, and insert the tables in the ORM way. 



## Solution (this should be sent afterwards with your explanation video (if applicable)

In the `api_app_orm.py` file you can see the ORM implementation of the API. Some interesting facts to notice:
1. There's no need for `schema.sql` file anymore to define the schema of the database, since this is taken care of by
`Event` and `Ticket`.
2. The code now is way more object-oriented than before allowing for faster development of new features, since there's
type hinting available, so you can see all methods and attributes of all the database querying method by accessing its
members (aka pressing "." after the db object.)
3. This allows syntax errors to come up before running the code, since everything is evaluated during typing. In the 
previous code if there was a syntax error within the SQL query string we would only find out by getting a more generic
error from the server during runtime. Fun fact, this happened many times during developing of the SQL-based example.

### Hint
Make sure to completely stop the api local server after running the `run.py` script.









