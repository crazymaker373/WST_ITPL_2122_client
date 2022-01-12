import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Command, BasicConfiguration
from datetime import datetime
import urllib.request
import subprocess

basicConf = BasicConfiguration()

# Create your views here.
@csrf_exempt
def set_Configuration(request):
    command = Command()

    command.command = request.POST.get("command")
    command.delay = request.POST.get("delay")
    command.save()

    if basicConf.stationId is None:
        basicConf.stationId = request.POST.get("stationId")

    if basicConf.serverUrl == '':
        basicConf.serverUrl = "http://localhost:8000/log"

    basicConf.save()

    result = subprocess.check_output(command.command, shell=True)

    postUrl(request, command, basicConf, result)

    return HttpResponse("hello")


def postUrl(request, command, basicConf, result):
    data = urllib.parse.urlencode({'message': result, 'createdAt': datetime.now(), 'stationId': basicConf.stationId, 'command': command.command, 'delay': command.delay})
    data = data.encode('utf-8')
    response = urllib.request.urlopen(basicConf.serverUrl, data)

    print(response.info())
