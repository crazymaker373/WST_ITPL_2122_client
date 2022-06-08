import datetime
import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Command, BasicConfiguration
from datetime import datetime
import urllib.request
from urllib.error import HTTPError
import subprocess

basicConf = BasicConfiguration()


# Create your views here.
@csrf_exempt
def set_Configuration(request):
    command = Command()

    command.command = request.POST.get('command')
    command.delay = request.POST.get('delay')
    command.save()

    if basicConf.stationId is None:
        basicConf.stationId = request.POST.get("stationId")

    if basicConf.serverUrl == '':
        basicConf.serverUrl = "http://192.168.3.72:8000"

    basicConf.save()

    if command.command.__contains__('ping'):
        command.command.replace('ping', 'ping -c 1')

    process = subprocess.run(command.command.split(' '),
                             stdout=subprocess.PIPE,
                             universal_newlines=True)
    result = process.stdout
    # result = subprocess.check_output(command.command, shell=True)

    data = urllib.parse.urlencode(
        {'message': result, 'createdAt': datetime.now(), 'stationId': basicConf.stationId, 'command': command.command,
         'delay': command.delay})
    data = data.encode('utf-8')
    try:
        response = urllib.request.urlopen(basicConf.serverUrl + '/log', data)
    except HTTPError as e:
        content = e.read()
        return HttpResponse(content)

    return HttpResponse(response)
