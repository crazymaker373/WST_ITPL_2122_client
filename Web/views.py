from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Command
import urllib.request
import os

# Create your views here.
@csrf_exempt
def set_Configuration(request):
    command = Command()

    command.command = request.POST.get("command")
    command.save()

    result = os.system(command.command)
    postUrl(request, result)
    return HttpResponse("Hello")

def postUrl(request, log):
    data = urllib.parse.urlencode({'station': log})
    data = data.encode('ascii')
    response = urllib.request.urlopen("http://localhost:8000/Web/log/", data)

    print(response.info())
