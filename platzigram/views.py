from curses.ascii import HT
from email import message
import numbers
from django.http import HttpResponse
from datetime import date, datetime

def hello_world(request):
    fechaActual = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse (f'¡Hello, world! la hora es {fechaActual}')

def hi(request):
    numbers = [request.GET['numbers']]
    return HttpResponse(str(numbers))

def say_hi(request, name, age):
    if age < 12:
        message = (f'Sorry {name}, you are not allowed here')
    else:
        message = (f'Hello, {name}! Welcome to Platzigram')
    return HttpResponse(message)







