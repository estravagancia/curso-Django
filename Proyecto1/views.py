from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object):
  def __init__(self,nombre, apellido) -> None:
     self.nombre = nombre
     self.apellido = apellido

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


# Lo anterior es para entender como funciona. No se hace así, se usan plantillas. Video 5
# para entenderlo -> (pero no se haría así tampoco, se usarían "cargadores")
def saludo_plantilla(request):
    doc_externo = open("C:/inetpub/desarrollo/django/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

#  vídeo 6
# uso de variables en plantillas
def saludo_plantilla_variables(request):
    nombre = "alberto"
    apellido = "Ibáñez"
    ahora = datetime.datetime.now()
    doc_externo = open("C:/inetpub/desarrollo/django/Proyecto1/Proyecto1/plantillas/miplantilla_variables.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    # hacemos uso de diccionarios: "clave": valor
    ctx = Context({"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual": ahora})
    documento = plt.render(ctx)
    return HttpResponse(documento)
# usando la clase Persona
def saludo_plantilla_clase(request):
    p1 = Persona("Stella Maris","Camelino Casco Bogado")
    ahora = datetime.datetime.now()
    doc_externo = open("C:/inetpub/desarrollo/django/Proyecto1/Proyecto1/plantillas/miplantilla_clase.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    # hacemos uso de diccionarios: "clave": valor
    ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora})
    documento = plt.render(ctx)
    return HttpResponse(documento)
  
  # video 7
def saludo_plantilla_lista(request):
    p1 = Persona("Maris","Camelino")
    temas_del_curso= ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    # temas_del_curso= []
    ahora = datetime.datetime.now()
    doc_externo = open("C:/inetpub/desarrollo/django/Proyecto1/Proyecto1/plantillas/miplantilla_lista.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    # hacemos uso de diccionarios: "clave": valor
    ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_del_curso})
    documento = plt.render(ctx)
    return HttpResponse(documento)
