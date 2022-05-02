Comands for starting:
1) pip install -r requirements.txt
2) Connecting DB (PostgreSQL) to Django in settings
3) python manage.py makemigrations
4) python manage.py migrate
5) python manage.py runserver


http://127.0.0.1:8000/swagger/ - openApi

GET (/offer/):
    optional params:
    price - (int) the necessary money
    deposit - (float) money on hand as a percentage of the loan
    term - (int) years of credit slavery