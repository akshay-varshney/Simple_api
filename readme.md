If you want to start making a simple API using Flask Python and Flow the SQL Database Along with it.


There are 4 different files in this project:
1. api.py -- This is to make the simple Api using flask and adding the dummy data in the code itself without using the database.
2. database_sql.py- How to use sqlite databse commands in python to connect the databse
3. books.db- Is the sample database which has information about different books and author
4. api_final.py- This file will help to make an api and how to use mysql database with this.

These 4 files can be used start with api.py and install flask on your system by running this command:
pip install flask
After this run the python code as >> python api.py
Run local server on the browser:  http://127.0.0.1:5000/

congrats Now you know how to make a simple API and what are it's steps.

Second on in place of dummy data let's just SQL Database Along with it.

database_sql.py shows how to use database.

Similarly now run>> python api_final.py
This will return all the books data in the jason format
http://127.0.0.1:5000/api/v1/resources/books/all

If you want to add particular query add like this:
http://127.0.0.1:5000/api/v1/resources/books?published=2010

Hope you got the basics how to create the API using python and how we can add SQL database along with.




