
from django.http import HttpResponse
from datetime import datetime
import json

def fecha_y_hora(request):
	ahora=datetime.now().strftime("%b %dth , %Y - %H:%M hrs")
	return HttpResponse("fecha y hora: {ahora}".format(ahora=ahora))

def ordenar(request):
	numeros=request.GET["numeros"]
	numeros=sorted([int(i) for i in numeros.split(",")])
	datos={
		"estatus":"ok",
		"numeros":numeros,
		"mensaje": "integer sorted successfully."
	}
	import pdb; pdb.set_trace()
	return HttpResponse(
			json.dumps(str(datos)),
			content_type="application/json"
		)

def	hola_mundo(request,nombre,edad):
	if edad<12:
		mensaje="lo siento: {} tu no tienes la edad suficiente".format(nombre)
		
	else:
		mensaje="hola {} bienvenido aqui".format(nombre)

	return HttpResponse(mensaje)