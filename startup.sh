python -m install --upgrade pip

pip freeze > requirements

python -m pip install -r requirements
python manage.py makemigrations

python manage.py migrate

python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('client', '', 'client')" | python manage.py shell

winpty python.exe manage.py runserver 8001
