from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
import json


@csrf_exempt
def pagina_de_prueba(request):
    return HttpResponse("<h2>AAAAAAAAAAAAAAAAAA</h2>")


# -----------------------------
# CRUD de eventos
# -----------------------------

@csrf_exempt
def listar_eventos(self):
    # sacamos toda la informacion de la tabla eventos
    eventos = Teventos.objects.all()

    data = [{"id": p.id, "titulo": p.titulo, "imagen": p.imagen,
             "calendario": p.calendario, "asistentes_maximos": p.asistentes_maximos,
             "descripcion": p.descripcion,
             "organizador": p.organizador.first_name} for p in eventos]
    return JsonResponse(data, safe=False)

@csrf_exempt
def info_evento_individual(request, id):
    # @param id - id de evento del que mostraremos informacion

    # Teventos.objects.get(id=id) -> "de la tabla eventos saca lo que sea cuyo id sea el id que pasamos como parametro"
    evento = Teventos.objects.get(id=id)

    data = {"id": evento.id, "titulo": evento.titulo, "imagen": evento.imagen,
            "calendario": evento.calendario, "asistentes_maximos": evento.asistentes_maximos,
            "descripcion": evento.descripcion,
            "organizador": evento.organizador.first_name}
    return JsonResponse(data)


# @login_required() !! comprobar tipo=organizador
@csrf_exempt
def crear_evento(request):
    if request.method == "POST":
        # data = JSON del body "itemizado" para poder acceder a lo que sea que pasamos en el body del mensaje
        data = json.loads(request.body)

        # org = organizador (lo sacamos de data) org = texto puro, NO JSON
        org = Tusuarios.objects.get(id=data["organizador"])

        evento = Teventos.objects.create(
            titulo=data["titulo"],
            imagen=data["imagen"],
            calendario=datetime.now(),
            asistentes_maximos=data["asistentes_maximos"],
            descripcion=data["descripcion"],
            organizador=org
        )
        # exito: titulo del evento creado + id (para verlo facilmente en postman)
        return JsonResponse({"id": evento.id, "titulo": evento.titulo, "mensaje": "creado"})
    else:

        return JsonResponse({"mensaje": "Algo ha fallado!"})


# @login_required() !!comprobar tipo=organizador
@csrf_exempt
def actualizar_evento(request, id):
    # @param id - id de evento que vamos a actualizar

    if request.method in ["PUT", "PATCH"]:
        data = json.loads(request.body)

        # debido a que organizador no es texto puro (es un objeto / FK en la tabla) para poder crear el evento correctamente,
        # primero debemos obtener la instancia de la tabla, para que asi django reciba el objeto "usuario" entero y no el valor de usuario que tiene evento (que es el id del organizador)
        organizador = Tusuarios.objects.get(id=data["organizador"])

        # actualizamos el evento
        evento = Teventos.objects.get(id=id)
        evento.titulo = data.get("titulo", evento.titulo)
        evento.imagen = data.get("imagen", evento.imagen)
        evento.calendario = data.get("calendario", evento.calendario)
        evento.asistentes_maximos = data.get("asistentes_maximos", evento.asistentes_maximos)
        evento.descripcion = data.get("descripcion", evento.descripcion)

        # organizador = OBJETO organizador (cuya id pasamos en el body) obtenido anteriormente (L87)
        evento.organizador = organizador

        # Guardamos el evento actualizado
        evento.save()

        # devolvemos informacion del evento actualizada
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
                             "mensaje": "Evento eliminado"})


# ------------------------------
# GESTION DE RESERVAS
# ------------------------------


# METODO GET @login_required() PERO puede ser org o asistente
@csrf_exempt
def listar_reservas(request, id):
    # @param id - id de usuario para listar sus reservas

    if request.method == "GET":

        # sacamos todas las reservas de la tabla
        reservas = Treservas.objects.all()

        # creamos una lista para ir guardando las reservas del usuario que buscamos
        lista_reservas = []

        # Si el id coincide, añadimos la informacion de la reserva a la lista (formato JSON)
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

        # Sacamos instancias del usuario que reserva y el evento que reserva para crear el objeto
        usuario_reserva = Tusuarios.objects.get(id=data["usuario"])
        evento_reserva = Teventos.objects.get(id=data["reserva"])

        reserva = Treservas.objects.create(
            evento=evento_reserva,
            usuario=usuario_reserva,
            entradas_reservadas=data["entradas_reservadas"],
            tipo=data["tipo_reserva"],
        )
        return JsonResponse({"id": reserva.id, "titulo": reserva.evento.titulo, "mensaje": "reserva creada"})


@csrf_exempt
def actualizar_reserva(request, id):
    # @param id - id de reserva para actualizar

    if request.method in ["PUT", "PATCH"]:
        data = json.loads(request.body)

        usuario_reserva = Tusuarios.objects.get(id=data["usuario"])
        evento_reserva = Teventos.objects.get(id=data["evento"])

        reserva = Treservas.objects.get(id=id)
        reserva.evento = evento_reserva
        reserva.usuario = usuario_reserva
        reserva.entradas_reservadas = data.get("entradas_reservadas", reserva.entradas_reservadas)
        reserva.tipo = data.get("tipo_reserva")
        reserva.save()
        return JsonResponse({"id": reserva.id, "nombre_reserva": reserva.evento.titulo,
                             "mensaje": "Reserva actualizada"})


@csrf_exempt
def eliminar_reserva(request, id):
    # @param id - id de reserva a eliminar

    if request.method == "DELETE":
        reserva = Treservas.objects.get(id=id)
        reserva.delete()
        return JsonResponse({"mensaje": "Reserva eliminada"})


# ----------------------
# GESTION DE COMENTARIOS
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
    else:
        data = json.loads(request.body)
        usuario_reserva = Tusuarios.objects.get(id=data["usuario"])
        evento_reserva = Teventos.objects.get(id=data["evento"])

        comentario = Tcomentarios.objects.get(id=id)
        comentario.comentario = data['nuevo_comentario']
        comentario.evento = Tcomentarios.objects.get(id=id)
        comentario.usuario = data["usuario"]
        comentario.save()
    return JsonResponse({"status": "ok"})


# ----------------------
# GESTION DE USUARIOS
# ----------------------
@csrf_exempt
def login_usuario(request):
    data = json.loads(request.body)

    usuario = data["username"]
    contra = data["password"]

    user = authenticate(username=usuario, password=contra)

    if user is not None:
        login(request, user)
        return JsonResponse({"status": "Login !!!!!!"})
    else:
        return JsonResponse({"status": "Login fallido"})


@csrf_exempt
def crear_usuario(request):
    # Sacamos el user model para crear el usuario mas tarde
    Usuario = get_user_model()

    lista_usuarios = Tusuarios.objects.all()
    data = json.loads(request.body)

    nombre_usuario = data["username"]
    correo = data["email"]
    contra = data["password"]
    nickname = data["first_name"]

    # si el usuario existe en lista_usuarios, registro fallido
    if lista_usuarios.filter(username=nombre_usuario).exists():
        return JsonResponse({"status": "Registro fallido (nombre de usuario en uso)"})
    else:
        Usuario.objects.create_user(username=nombre_usuario, email=correo, password=contra, first_name=nickname)
        return JsonResponse({"status": "Usuario registrado con exito"})



# ----------------------
# Utilizando APIView
# ----------------------

# ----------------------
# GESTION DE EVENTOS (APIVIEW)
# ----------------------
class ListarEventosAPIView(APIView):
    def get(self, request):
        eventos = Teventos.objects.all()
        data = [{"id": p.id, "titulo": p.titulo, "imagen": p.imagen,
                 "calendario": p.calendario, "asistentes_maximos": p.asistentes_maximos,
                 "descripcion": p.descripcion,
                 "organizador": p.organizador.first_name} for p in eventos]
        return Response(data)