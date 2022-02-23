#!/bin/bash
python manage.py migrate
#python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('client', '', 'client')" | python manage.py shell
#echo "import urllib.request; urllib.request.urlopen('http://192.168.102.145:8000/setstation', urllib.parse.urlencode({'url': '192.168.192.213'}).encode('utf-8'))" | python manage.py shell
echo "import urllib.request; urllib.request.urlopen('http://192.168.100.8:8000/setstation/' + '192.169.1243')" | python manage.py shell
python manage.py runserver 8001
