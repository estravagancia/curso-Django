from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request): # primera vista
    documento = "Hola mundo. Mi primera página con django"
    return HttpResponse(documento)


def despedida(request): # primera vista
  documento = """<html>
  <body>
  <h1>
  Hasta luegoooooo. Mi primera página con django
  </h1>
  </body>
  </html>"""
  return HttpResponse(documento)


def dame_fecha(request):
  fecha_actual = datetime.datetime.now()
  documento = """<html>
  <body>
  <p>
  Fecha y hora actuales %s
  </p>
  </body>
  </html>""" % fecha_actual
  return HttpResponse(documento)


# con 1 parámetro: any
def muestra_edad(request , any):
  edad_actual = 51
  periodo = any - 2022
  edad_futura = edad_actual + periodo
  documento = "<html><body>En el año %s tendrás %s años</body></html>" %(any , edad_futura)
  return HttpResponse(documento)

# con 2 parámetros: edad , any

def calcula_edad(request , edad, any):
  periodo = any - 2022
  edad_futura = edad + periodo
  documento = "<html><body>En el año %s tendrás %s años</body></html>" %(any , edad_futura)
  return HttpResponse(documento)


# Lo anterior es para entender como funciona. No se hace así, se usan plantillas.
# para entenderlo -> (pero no se haría así tampoco, se usarían "cargadores")
def saludo_plantilla(request):
    doc_externo = open("C:/inetpub/desarrollo/django/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

