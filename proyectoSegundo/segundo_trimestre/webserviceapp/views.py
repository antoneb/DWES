from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
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
    # @param id - id de evento para mostrar su informacion
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
    # @param id - id de evento para actualizar
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
    # @param id - id de evento  para eliminar
    if request.method == "DELETE":
        evento = Teventos.objects.get(id=id)
        evento.delete()
        return JsonResponse({"id": evento.id, "titulo": evento.titulo,
                             "mensaje": "Producto eliminado"})


# ------------------------------
# GESTION DE RESERVAS
# ------------------------------


# METODO GET !!!! @login_required() PERO puede ser org o asistente
@csrf_exempt
def listar_reservas(request, id):
    # @param id - id de usuario para ver sus reservas
    if request.method == "GET":

        reservas = Treservas.objects.all()
        lista_reservas = []

        for r in reservas:
            if r.usuario.id == id:
                reserva_ind = {}
                reserva_ind["id"] = r.id
                reserva_ind["evento"] = r.evento.titulo
                reserva_ind["organizador"] = r.evento.organizador.first_name
                reserva_ind["usuario_reservante"] = r.usuario.first_name
                reserva_ind["entradas_reservadas"] = r.entradas_reservadas
                reserva_ind["estado_reserva"] = r.tipo
                lista_reservas.append(reserva_ind)

        return JsonResponse(lista_reservas, safe=False)


# METODO POST
@csrf_exempt
def crear_reserva(request):
    if request.method == "POST":
        data = json.loads(request.body)
        reserva = Treservas.objects.create(
            evento=data["evento"],
            usuario=data["usuario"],
            entradas_reservadas=data["entradas_reservadas"],
            tipo=data["tipo"],
        )
        return JsonResponse({"id": reserva.id, "titulo": reserva.titulo, "mensaje": "reserva creada"})


@csrf_exempt
def actualizar_reserva(request, id):
    # @param id - id de reserva para actualizar
    if request.method in ["PUT", "PATCH"]:
        data = json.loads(request.body)
        reserva = Treservas.objects.get(id=id)
        reserva.evento = data.get("evento", reserva.evento)
        reserva.usuario = data.get("usuario", reserva.usuario.first_name)
        reserva.entradas_reservadas = data.get("entradas_reservadas", reserva.entradas_reservadas)
        reserva.save()
        return JsonResponse({"id": reserva.id, "nombre_reserva": reserva.evento.titulo,
                             "mensaje": "Reserva actualizada"})


@csrf_exempt
def eliminar_reserva(request, id):
    # @param id - id de reserva a eliminar
    if request.method == "DELETE":
        reserva = Treservas.objects.get(id=id)
        reserva.delete()
        return JsonResponse({"id": reserva.id, "usuario_reservador": reserva.usuario,
                             "mensaje": "Reserva actualizada"})


# ----------------------
# GESTION COMENTARIOS
# ----------------------

@csrf_exempt
def listar_comentarios_evento(request, id):
    # @param id - id de evento del que queremos ver comentarios
    if request.method == "GET":

        comentarios = Tcomentarios.objects.all()
        lista_comentarios = []

        for r in comentarios:
            if r.evento.id == id:
                comentario_ind = {}
                comentario_ind["id"] = r.id
                comentario_ind["evento"] = r.evento.titulo
                comentario_ind["usuario"] = r.usuario.first_name
                comentario_ind["comentario"] = r.comentario
                lista_comentarios.append(comentario_ind)

        return JsonResponse(lista_comentarios, safe=False)


@csrf_exempt
def guardar_comentario(request, id):
    # @param id - id de evento que vamos a comentar
    if request.method != "POST":
        return None
    data = json.loads(request.body)
    comentario = Tcomentarios()
    comentario.comentario = data['nuevo_comentario']
    comentario.evento = Tcomentarios.objects.get(id=id)
    comentario.usuario = data["usuario"]
    comentario.save()
    return JsonResponse({"status": "ok"})

# ----------------------
# GESTION DE USUARIOS
# ----------------------

def login_usuario(request):
    usuario = request.POST["username"]
    contra = request.POST["password"]
    user = authenticate(request,username=usuario,password=contra)
    if user is not None:
        login(request,user)
        return JsonResponse({"status": "Login !!!!!!"})
    else:
        return JsonResponse({"status":"Login fallido"})

