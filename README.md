#API Test Django

## Technologies
- Python 3.8+
- Django 4.2

## Enviroment Setup
    - python -m venv <venv>
    # for Linux OS
    - source venv/bin/activate 
    # for Window OS
    - source venv/Scripts/activate
    - pip install -r requirement.txt
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver


## API Endpoints
    - {baseUrl}/api/challenges/list
    - {baseUrl}/api/challenges/{id}
