# Questions App
App for question_listing [GET, POST, PUT, DELETE] with auth-JWT enabled. 
## Quickstart

To work in a sandboxed Python environment it is recommended to install the app in a Python [virtualenv](https://pypi.python.org/pypi/virtualenv).

1. Install dependencies

    ```bash
    $ cd /path/to/question_listing
    $ pip install -r requirements.txt
    ```

1. Setup a sqlite database 

  ```Sql
environment = [dev, test, prod]  
export CONFIG_TYPE=[environment]

python manage.py db_init

```


1. Running app

   ```bash
   $ python manage.py run
   ```

   View for API documentation ```http://127.0.0.1:5000/api/v1/ ```
      

## Project Structure

### Backend 
```shell
question_listing/                          # All application code in this directory.
│
├─app                                      # Shared/misc code goes in here as packages or modules.
│  ├── __init__.py                         
│  └─ v1    ──────┐                        # version 1 for API
│                 ├─ models/               # Holds several tables about a subject.
│                 │  ├─ auth.py            
│                 │  ├─ question.py        
│                 │  └─ user.py            
│                 ├─ resources/            # Holds several resource files for API
│                 │  ├─ auth.py            
│                 │  ├─ question.py        
│                 │  └─ user.py           
│                 ├─ exceptions.py         # exceptions file    
│                 ├─ utils.py              # Holds JWT access files
│                 └─ __init__.py                                
├─ tests/                                  # Tests are structured similar to the application.
├─ config.py                               # All configs for Flask, Test, Prod, Dev, etc.
├─ requirements.txt                        # requirements file
└─ manage.py                               # Main entry-point into the Flask application.
```

##  Design 

The boilerplate used for this app is [Flask-Large-Application-Example](https://github.com/Robpol86/Flask-Large-Application-Example).<br />
I have used [python-pandemonium](https://medium.com/python-pandemonium/json-web-token-based-authentication-in-django-b6dcfa42a332) medium article for implementing PyJWT.<br />
Features:
1. Expandable, understandable and project structure with that of Django styled with namespaces and blueprints.
2. Auth with JWT with refresh tokens and supporting multiple devices of the same user.
3. Custom ValidationExeption and exception handler for example.
4. Tests (Will be updated in sometime).
5. Database interaction with Flask-SQLAlchemy.  






