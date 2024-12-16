from os import system

system('pip install poetry')

system('poetry install')

system(r'python .\manage.py makemigrations')

system(r'python .\manage.py migrate')

system(
    r'python .\manage.py createsuperuser'
    r' --username admin --password admin --email admin@admin.ru --first_name admin'
)
