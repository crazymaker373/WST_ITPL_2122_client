python -m pip install --upgrade pip

pip freeze > requirements

python -m pip install -r requirements
python manage.py makemigrations

python manage.py migrate

python manage.py syncdb --noinput

echo "from django.contrib.auth.models import User; User.objects.create_superuser('client', '', 'client')" | python manage.py shell

winpty python.exe manage.py runserver 8001

apt update
apt install -y dnsutils
apt-get install curl
curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash
apt install -y speedtest

echo "import urllib.request; urllib.request.urlopen('http://192.168.3.72:8000/setstation', urllib.parse.urlencode({'url': '192.168.5.228:8001'}).encode('utf-8'))" | python manage.py shell
