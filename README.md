# frest
How to create a REST API very quickly.

## Installation
Install **frest** by pip package (you must have Python>=3.6). In this example I'm using [virtualev](https://pypi.org/project/virtualenv/), a tool for virtual environment creation.
```
$ virtualenv env
$ source env/bin/activate
(env) $ pip install frest
```

## Use
#### Create a project
```
(env) $ frest --init project                                                                                                                                                
  
   __               _    
  / _|             | |   
 | |_ _ __ ___  ___| |_ 
 |  _| '__/ _ \/ __| __| 
 | | | | |  __/\__ \ |_  
 |_| |_|  \___||___/\__|
    


Create project/... OK
Create project/__init__.py... OK

```
It will create a project tree folder like this one:
* database.py
	A file with DATABASE_URI, database path, default is `sqlite:///database.db`.
* mail.py
	A file with mail configuration: server, port, password etc.
* app.py
	A file with routes and mail/database configuration.
* wsgi.py
	File used for production.

#### Create first app
Inside `project` folder, we start to create a new app. For example, we want to store books inside our database.
```
(env) $ cd project/
(env) $ frest --startapp book
```

It will print something like this:
```
   __               _    
  / _|             | |   
 | |_ _ __ ___  ___| |_ 
 |  _| '__/ _ \/ __| __| 
 | | | | |  __/\__ \ |_  
 |_| |_|  \___||___/\__|
    


Create scheme/... OK
Create scheme/book... OK
Create scheme/book/__init__.py... OK
Create model for book...
Fields id, created_at, updated_at are default on every new model, you can delete it from model file

Create field? (Y/n): 
```
Now we have to define a model for our `book`, using 6 data types: integer, string, text, datetime, float, bool.
This is an example of our `book` with **name** and **pubblication date**:
```
Choose field name: name
Choose field type: int, str, text, datetime, float, bool str
Choose string size: 20
Field is nullable? (Y/n): n
Create new field? (Y/n): 
Choose field name: pubblication_date
Choose field type: int, str, text, datetime, float, bool datetime
Field is nullable? (Y/n): n
Create new field? (Y/n): n
Create scheme/book/models.py... OK
Create scheme/book/forms.py... OK
Create scheme/book/routes.py... OK
```

Now, our book it will be inside `scheme/book`.

#### Move scheme routes inside app
Edit `project/app.py` and put your routes inside.
```
[...]
from frest.auth.routes import api as api_users
from scheme.book.routes import api as api_books
[...]
app.register_blueprint(api_books)
[...]
```

#### Database creation
Open python interpreter, import db and create.
```
from app import db
db.create_all()
```
Now exit and check your scheme inside database. It will be something like this.
```
CREATE TABLE user (
	"userId" INTEGER NOT NULL, 
	email VARCHAR(30), 
	password VARCHAR(30), 
	is_admin BOOLEAN, 
	name VARCHAR(30), 
	created_at DATETIME, 
	PRIMARY KEY ("userId"), 
	CHECK (is_admin IN (0, 1))
);
CREATE TABLE book (
	"bookId" INTEGER NOT NULL, 
	name VARCHAR(20) NOT NULL, 
	pubblication_date DATETIME NOT NULL, 
	created_at DATETIME, 
	updated_at DATETIME, 
	PRIMARY KEY ("bookId")
);
CREATE TABLE token (
	"tokenId" INTEGER NOT NULL, 
	string VARCHAR(20), 
	created_at DATETIME, 
	expired BOOLEAN, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY ("tokenId"), 
	CHECK (expired IN (0, 1)), 
	FOREIGN KEY(user_id) REFERENCES user ("userId")
);
```

#### Start app
Inside `project` file you have to run `python app.py` and it's done.

## TODO

 - [ ] Migrations of database in case of edits
 - [ ] Put automatically `routes` inside app file
 - [ ] More datatype
 - [ ] Relantionships (1-to-1, 1-to-n, n-to-n)


