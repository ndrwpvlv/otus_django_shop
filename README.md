#otus_django_shop
**otus_django_shop** is simple example of django usage for online shop creation. 
It uses Django admin panel to organize products and categories input.

Homework-shop based on Django framework.

Now it demonstrate index, catalog, categories and products pages only. 

## Installation
Download source or clone this repository as working directory.

## Before start
First you need to organize virtual environment with requirements.txt.

Second you need to make database and fill it with initial data. From project console 
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_data.json
```

## Basic usage
Run with console:
```
python manage.py runserver
```
To create superuser run: 
```
python manage.py createsuperuser
```

Server is configured to run on http://127.0.0.1:8000/.

Admin dashboard: http://127.0.0.1:8000/admin/



## Requirements
```
Python 3.5+

Django==2.2.2
pytz==2019.1
sqlparse==0.3.0
```

## Contributors
Andrei S. Pavlov (https://github.com/ndrwpvlv/)
 