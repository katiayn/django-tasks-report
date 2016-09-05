# Django Tasks Report

1) Configure virtualenv:

```
$ pip install virtualenv
$ python -m venv .dtr
$ source .dtr/bin/activate
```

2) Install the requirements:

```
$ pip install -r requirements.txt
```

3) Generate a secret key using [this link](http://www.miniwebtool.com/django-secret-key-generator/)

4) Create a .env file with the following content:

```
SECRET_KEY=<YOUR_SECRET_KEY_GOES_HERE>
DEBUG=True
```

5) Run the migrations:

```
$ python manage.py migrate
```

6) Run the project:

```
$ python manage.py runserver
```
