from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
import json


# Create your views here.


@csrf_exempt
def pagina_de_prueba(request):
    return HttpResponse("<h2>AAAAAAAAAAAAAAAAAA</h2>")


# ~----------------------------
# CRUD de eventos
# -----------------------------

@csrf_exempt
def listar_eventos(self):
    eventos = Teventos.objects.all()
    data = [{"id": p.id, "titulo": p.titulo, "imagen": p.imagen,
             "calendario": p.calendario, "asistentes_maximos": p.asistentes_maximos,
             "descripcion": p.descripcion,
             "organizador": p.organizador.first_name} for p in eventos]
    return JsonResponse(data, safe=False)


@csrf_exempt
def info_evento_individual(request, id):
    evento = Teventos.objects.get(id=id)
    data = {"id": evento.id, "titulo": evento.titulo, "imagen": evento.imagen,
            "calendario": evento.calendario, "asistentes_maximos": evento.asistentes_maximos,
            "descripcion": evento.descripcion,
            "organizador": evento.organizador.first_name}
    return JsonResponse(data)


# @login_required() !!comprobar tipo=organizador
@csrf_exempt
def crear_evento(request):
    if request.method == "POST":
        data = json.loads(request.body)
        evento = Teventos.objects.create(
            titulo=data["titulo"],
            imagen=data["imagen"],
            calendario=data["calendario"],
            asistentes_maximos=data["asistentes_maximos"],
            descripcion=data["descripcion"],
            organizador=data["organizador"],
        )
        return JsonResponse({"id": evento.id, "titulo": evento.titulo, "mensaje": "creado"})


# @login_required() !!comprobar tipo=organizador
@csrf_exempt
def actualizar_evento(request, id):
    if request.method in ["PUT", "PATCH"]:
        data = json.loads(request.body)
        evento = Teventos.objects.get(id=id)
        evento.titulo = data.get("titulo", evento.titulo)
        evento.imagen = data.get("imagen", evento.imagen)
        evento.calendario = data.get("calendario", evento.calendario)
        evento.asistentes_maximos = data.get("asistentes_maximos", evento.asistentes_maximos)
        evento.descripcion = data.get("descripcion", evento.descripcion)
        evento.organizador = data.get("organizador", evento.organizador.first_name)
        evento.save()
        return JsonResponse({"id": evento.id, "titulo": evento.titulo,
                             "mensaje": "Evento actualizado"})


# @login_required() !!comprobar tipo=organizador
@csrf_exempt
def eliminar_evento(request, id):
    if request.method == "DELETE":
        evento = Teventos.objects.get(id=id)
        evento.delete()
        return JsonResponse({"id": evento.id, "titulo": evento.titulo,
                             "mensaje": "Producto eliminado"})


# ------------------------------
# GESTION DE RESERVAS
# ------------------------------


@csrf_exempt
# @login_required() PERO puede ser org o asistente
def listar_reservas(request, id):
    if request.method == "GET":
        data = json.loads(request.body)
        #crea
        reservas_usuario = {}
        reservas = Treservas.objects.getAll()
        for r in reservas:
            if (r.usuario.id == id):
                reservas_usuario.add(r)

        return JsonResponse(reservas_usuario)
