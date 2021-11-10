from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Command

# Create your views here.
@csrf_exempt
def Set_Configuration(request):
    command = Command()

    command.command = request.POST.get("command")
    command.save()

    return HttpResponse("Hello")
