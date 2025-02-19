from http.client import responses

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

from datetime import datetime

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
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
    @swagger_auto_schema(
        operation_description="Lista eventos. Filtra por fecha u organizador",
        manual_parameters=[
            openapi.Parameter('fecha', openapi.IN_QUERY, description="Filtrar por fecha (YYYY-MM-DD)", format="date-time",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('organizador', openapi.IN_QUERY, description="Filtrar por nombre de organizador", type=openapi.TYPE_STRING),
        ],
        responses={201: openapi.Response(description="Evento creado"),
                   403: openapi.Response(description="No tienes permisos para crear eventos.")}
    )
    def get(self, request):
        eventos = Teventos.objects.all()
        data = [{"id": p.id, "titulo": p.titulo, "imagen": p.imagen,
                 "calendario": p.calendario, "asistentes_maximos": p.asistentes_maximos,
                 "descripcion": p.descripcion,
                 "organizador": p.organizador.first_name} for p in eventos]
        return Response(data)


class InfoEventoIndividualAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Obtener informacion evento individual",
        responses={200: openapi.Response("Informacion evento")},
    )
    def get(self, request, id):
        try:
            evento = Teventos.objects.get(id=id)
            data = {
                "id": evento.id,
                "titulo": evento.titulo,
                "imagen": evento.imagen,
                "calendario": evento.calendario,
                "asistentes_maximos": evento.asistentes_maximos,
                "descripcion": evento.descripcion,
                "organizador": evento.organizador.first_name
            }
            return Response(data)

        except Teventos.DoesNotExist:
            return Response({"detail": "No se ha encontrado un evento con ese id."}, status=status.HTTP_404_NOT_FOUND)


class CrearEventoAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Crea un nuevo evento.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'titulo': openapi.Schema(type=openapi.TYPE_STRING, description='Título del evento'),
                'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description='Descripción del evento'),
                'calendario': openapi.Schema(type=openapi.TYPE_STRING, format="date-time",
                                             description='Fecha y hora del evento'),
                'asistentes_maximos': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                     description='Capacidad máxima de asistentes'),
                'organizador': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID de usuario organizador')
            },
            required=['titulo', 'descripcion', 'calendario', 'asistentes_maximos']
        ),
        responses={201: openapi.Response(description="Evento creado"),
                   403: openapi.Response(description="No tienes permisos para crear eventos.")}
    )
    def post(self, request):
        try:
            organizador = Tusuarios.objects.get(id=request.data.get('organizador'))

            evento = Teventos.objects.create(
                titulo=request.data.get('titulo'),
                imagen=request.data.get('imagen'),
                calendario=request.data.get('calendario'),
                asistentes_maximos=request.data.get('asistentes_maximos'),
                descripcion=request.data.get('descripcion'),
                organizador=organizador
            )
            return Response({"id": evento.id, "titulo": evento.titulo, "mensaje": "creado"},
                            status=status.HTTP_201_CREATED)

        except Tusuarios.DoesNotExist:
            return Response({"detail": "No se ha encontrado un usuario con ese id."}, status=status.HTTP_404_NOT_FOUND)

        except KeyError as e:
            return Response({"detail": f"campo vacio: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class ActualizarEventoAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Actualizar evento",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'titulo': openapi.Schema(type=openapi.TYPE_STRING, description='Título del evento'),
                'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description='Descripción del evento'),
                'calendario': openapi.Schema(type=openapi.TYPE_STRING, format="date-time",
                                             description='Fecha y hora del evento'),
                'asistentes_maximos': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                     description='Capacidad máxima de asistentes'),
                'organizador': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID de usuario organizador')
            },
            required=['titulo']
        ),
        responses={200: openapi.Response("Evento actualizado")},
    )
    def put(self, request, id):
        try:
            evento = Teventos.objects.get(id=id)

            organizador = Tusuarios.objects.get(id=request.data.get('organizador'))

            evento.titulo = request.data.get('titulo')
            evento.imagen = request.data.get('imagen')
            evento.calendario = request.data.get('calendario')
            evento.asistentes_maximos = request.data.get('asistentes_maximos')
            evento.descripcion = request.data.get('descripcion')
            evento.organizador = organizador

            evento.save()

            return Response({"id": evento.id, "titulo": evento.titulo, "mensaje": "Evento actualizado"})

        except Teventos.DoesNotExist:
            return Response({"detail": "No se ha encontrado un evento con ese id."}, status=status.HTTP_404_NOT_FOUND)

        except Tusuarios.DoesNotExist:
            return Response({"detail": "No se ha encontrado un organizador/usuario con ese id."},
                            status=status.HTTP_404_NOT_FOUND)

        except KeyError as e:
            return Response({"detail": f"campo vacio: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class EliminarEventoAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Elimina un evento",
        responses={200: openapi.Response("Elimina un evento")},
    )
    def delete(self, request, id):
        try:
            evento = Teventos.objects.get(id=id)
            evento.delete()
            return Response({"id": evento.id, "titulo": evento.titulo, "mensaje": "Evento eliminado"})

        except Teventos.DoesNotExist:
            return Response({"detail": "No se ha encontrado un evento con ese id."}, status=status.HTTP_404_NOT_FOUND)


# ----------------------
# GESTION DE RESERVAS (APIVIEW)
# ----------------------

class ListarReservasAPIView(APIView):
    def get(self, request, id):
        reservas = Treservas.objects.filter(usuario_id=id)
        lista_reservas = []

        for reserva in reservas:
            reserva_ind = {
                "id": reserva.id,
                "evento": reserva.evento.titulo,
                "organizador": reserva.evento.organizador.first_name,
                "usuario_reservante": reserva.usuario.first_name,
                "entradas_reservadas": reserva.entradas_reservadas,
                "estado_reserva": reserva.tipo
            }
            lista_reservas.append(reserva_ind)
        return Response(lista_reservas)


class CrearReservaAPIView(APIView):
    def post(self, request):
        try:

            usuario_reserva = Tusuarios.objects.get(id=request.data.get('usuario'))
            evento_reserva = Teventos.objects.get(id=request.data.get('reserva'))

            reserva = Treservas.objects.create(
                evento=evento_reserva,
                usuario=usuario_reserva,
                entradas_reservadas=request.data.get('entradas_reservadas'),
                tipo=request.data.get('tipo_reserva')
            )
            return Response({"id": reserva.id, "titulo": reserva.evento.titulo, "mensaje": "reserva creada"},
                            status=status.HTTP_201_CREATED)

        except Tusuarios.DoesNotExist:
            return Response({"detail": "No se ha encontrado un usuario con ese id."}, status=status.HTTP_404_NOT_FOUND)

        except Teventos.DoesNotExist:
            return Response({"detail": "No se ha encontrado un evento con ese id."}, status=status.HTTP_404_NOT_FOUND)

        except KeyError as e:
            return Response({"detail": f"Campo vacio: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class ActualizarReservaAPIView(APIView):
    def put(self, request, id):
        try:

            usuario_reserva = Tusuarios.objects.get(id=request.data.get('usuario'))
            evento_reserva = Teventos.objects.get(id=request.data.get('evento'))

            reserva = Treservas.objects.get(id=id)
            reserva.evento = evento_reserva
            reserva.usuario = usuario_reserva
            reserva.entradas_reservadas = request.data.get("entradas_reservadas")
            reserva.tipo = request.data.get("tipo_reserva")
            reserva.save()

            return Response(
                {"id": reserva.id, "nombre_reserva": reserva.evento.titulo, "mensaje": "Reserva actualizada"})
        except Treservas.DoesNotExist:
            return Response({"detail": "No se ha encontrado una reserva con ese id."}, status=status.HTTP_404_NOT_FOUND)
        except Tusuarios.DoesNotExist:
            return Response({"detail": "No se ha encontrado un usuario con ese id."}, status=status.HTTP_404_NOT_FOUND)
        except Teventos.DoesNotExist:
            return Response({"detail": "No se ha encontrado un evento con ese id."}, status=status.HTTP_404_NOT_FOUND)
        except KeyError as e:
            return Response({"detail": f"Campo vacio: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class EliminarReservaAPIView(APIView):
    def delete(self, request, id):
        try:
            reserva = Treservas.objects.get(id=id)
            reserva.delete()
            return Response({"mensaje": "Reserva eliminada"})
        except Treservas.DoesNotExist:
            return Response({"detail": "No se ha encontrado una reserva con ese id."},
                            status=status.HTTP_404_NOT_FOUND)


# ----------------------
# GESTION DE COMENTARIOS (APIVIEW)
# ----------------------
class ListarComentariosEventoAPIView(APIView):
    def get(self, request, id):
        comentarios = Tcomentarios.objects.filter(evento_id=id)
        lista_comentarios = []

        for comentario in comentarios:
            comentario_ind = {
                "id": comentario.id,
                "evento": comentario.evento.titulo,
                "usuario": comentario.usuario.first_name,
                "comentario": comentario.comentario
            }
            lista_comentarios.append(comentario_ind)
        return Response(lista_comentarios)


class GuardarComentarioAPIView(APIView):
    def post(self, request, id):
        try:
            usuario_comenta = Tusuarios.objects.get(id=request.data.get('usuario_comenta'))
            evento_comentado = Teventos.objects.get(id=request.data.get('evento_comentado'))

            comentario = Tcomentarios.objects.create(
                evento=evento_comentado,
                usuario=usuario_comenta,
                fechapost=request.data.get('fechapost'),
                comentario=request.data.get('comentario')
            )

            return Response({"id": comentario.id, "titulo": comentario.evento.titulo, "mensaje": "comentario creado"},
                            status=status.HTTP_201_CREATED)

        except Tusuarios.DoesNotExist:
            return Response({"detail": "No se ha encontrado un usuario con ese id."}, status=status.HTTP_404_NOT_FOUND)

        except Teventos.DoesNotExist:
            return Response({"detail": "No se ha encontrado un evento con ese id."}, status=status.HTTP_404_NOT_FOUND)

        except KeyError as e:
            return Response({"detail": f"Campo vacio: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


# ----------------------
# GESTION DE USUARIOS (APIVIEW)
# ----------------------
class LoginUsuarioAPIView(APIView):
    def post(self, request):

        usuario = request.data.get("username")
        contra = request.data.get("password")

        user = authenticate(username=usuario, password=contra)

        if user is not None:
            login(request, user)
            return Response({"status": "Login exitoso!"})
        else:
            return Response({"status": "Login fallido !"}, status=status.HTTP_401_UNAUTHORIZED)


class CrearUsuarioAPIView(APIView):
    def post(self, request):
        nombre_usuario = request.data.get("username")
        correo = request.data.get("email")
        contra = request.data.get("password")
        nickname = request.data.get("first_name")

        Usuario = get_user_model()

        # Check if the username already exists
        if Tusuarios.objects.filter(username=nombre_usuario).exists():
            return Response({"status": "Registro fallido: nombre de usuario ya existente"},
                            status=status.HTTP_400_BAD_REQUEST)

        Usuario.objects.create_user(username=nombre_usuario, email=correo, password=contra, first_name=nickname)

        return Response({"status": "Usuario registrado con exito"}, status=status.HTTP_201_CREATED)
