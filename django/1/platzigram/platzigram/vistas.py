
from django.http import HttpResponse
from datetime import datetime


def fecha_y_hora(request):
	ahora=datetime.now().strftime("%b %dth , %Y - %H:%M hrs")
	return HttpResponse("fecha y hora: {ahora}".format(ahora=ahora))

def hola_mundo(request):
	numeros=request.GET["numeros"]
	numeros=sorted([int(i) for i in numeros.split(",")])
	return HttpResponse(str(numeros))

