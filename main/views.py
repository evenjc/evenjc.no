from django.shortcuts import render
from django.http import HttpResponse

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Create your views here.

def index(request):
    return render(request, 'main/home.html')

def gpio(request):
    if (GPIO.input(17) == 0):
	str = "Knappen er inne"
    else:
	str = "Knappen er ute"
    return render(request, 'main/basic.html', {'c':str})

def handler404(request):
    response = handle_to_response('404.html', {},
					context_instance=RequestContext(request))
    response.status_code = 404
    return response


