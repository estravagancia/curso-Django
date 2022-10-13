from django.http import HttpResponse
import datetime
from django.template import Template, Context
# from django.template import loader
# haciendo más corto el loader
from django.template.loader import get_template

# video 9
from django.shortcuts import render
#  is equivalent to:
# from django.http import HttpResponse
# from django.template import loader


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
    p1 = Persona("Stella","Camelino")
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

  # video 8
def saludo_plantilla_condicionales(request):
    p1 = Persona("alberto","Ibáñez")
    temas_del_curso= ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    # temas_del_curso= []
    ahora = datetime.datetime.now()
    doc_externo = open("C:/inetpub/desarrollo/django/Proyecto1/Proyecto1/plantillas/miplantilla_condicionales.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    # hacemos uso de diccionarios: "clave": valor
    ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_del_curso})
    documento = plt.render(ctx)
    return HttpResponse(documento)


# usando loader. Basicamente consiste en decirle a nuestro proyecto, que las plantillas están en una ubicación. Nos ahorraremos el método open y close. 
# from django.template import loader
# Realizamos cambios en nuestro archivo settings.py en TEMPLATES -> DIRS indicando la ruta de las plantillas

def saludo_plantilla_loader(request):
    p1 = Persona("alberto","Ibáñez")
    temas_del_curso= ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    ahora = datetime.datetime.now()
    
    # debido a que usamos loader, cambian algunas cosas.
    
    # doc_externo = open("C:/inetpub/desarrollo/django/Proyecto1/Proyecto1/plantillas/miplantilla_loader.html")
    # plt = Template(doc_externo.read())
    
    # doc_externo = loader.get_template('miplantilla_loader.html')
    # con la versión corta - from django.template.loader import get_template

    doc_externo = get_template('miplantilla_loader.html')
    # doc_externo.close()
    
    # A pesar de que los 2 instancias son Template (plt = Template   &  loader.get_template), nos da error. 
    # No nos permite pasar un contexto, pasamos un diccionario -> renderizando directamente el diccionario, no necesitamos un Context
    # ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_del_curso})
    # documento = doc_externo.render(ctx)
    
    documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_del_curso})
    
    return HttpResponse(documento)
  
  # video 9
def saludo_plantilla_shortcut(request):
    p1 = Persona("alberto","Ibáñez")
    temas_del_curso= ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    ahora = datetime.datetime.now()
    
    # doc_externo = get_template('miplantilla_shortcut.html')
    
    # documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_del_curso})
    
    
    # modificamos HttpResponse pasa a ser render
    # return HttpResponse(documento)
    
    return render(request,'miplantilla_shortcut.html',{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_del_curso})
  
def saludo_plantilla_con_plantilla(request):
    p1 = Persona("alberto","Ibáñez")
    temas_del_curso= ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    ahora = datetime.datetime.now()
    
    # doc_externo = get_template('miplantilla_shortcut.html')
    
    # documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_del_curso})
    
    
    # modificamos HttpResponse pasa a ser render
    # return HttpResponse(documento)
    
    return render(request,'miplantilla_con_plantilla.html',{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_del_curso})
   
  # video 10
  # herencia de las plantillas {% extends "base.html" %}
def curso_django(request):
    ahora = datetime.datetime.now()
    
    return render(request,"curso-django.html",{"dame_fecha":ahora})
  
def curso_css(request):
    ahora = datetime.datetime.now()
    
    return render(request,"curso-css.html",{"dame_fecha":ahora})