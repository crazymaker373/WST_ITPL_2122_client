python -m install --upgrade pip

pip freeze > requirements

python -m pip install -r requirements
python manage.py makemigrations

python manage.py migrate

python manage.py syncdb --noinput

echo "from django.contrib.auth.models import User; User.objects.create_superuser('client', '', 'client')" | python manage.py shell

winpty python.exe manage.py runserver 8001

echo "import urllib.request; urllib.request.urlopen('http://localhost:8000/setstation', urllib.parse.urlencode({'url': '192.168.192.213'}).encode('utf-8'))" | python manage.py shell
