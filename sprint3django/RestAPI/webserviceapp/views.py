from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

# Create your views here.


def pagina_de_prueba(request):
    return HttpResponse("<h2>Que pasa tarantola</h2>")


def devolver_libros(request):
    listaLibros = Tlibros.objects.all()
    respuesta_final = []


    for fila_sql in listaLibros:
        diccionario = {}
        diccionario["id"] = fila_sql.id
        diccionario["titulo"] = fila_sql.titulo
        diccionario["imagen"] = fila_sql.imagen
        diccionario["anho"] = fila_sql.anho
        diccionario["genero"] = fila_sql.genero
        diccionario["autor"] = fila_sql.autor
        respuesta_final.append(diccionario)

    return JsonResponse(respuesta_final, safe=False)


def devolver_libro_por_id(request, id_solicitado):
    libro = Tlibros.objects.get(id=id_solicitado)
    comentarios = libro.tcomentarios_set.all()

    lista_comentarios = []

    for fila_sql in comentarios:
        diccionario = {}
        diccionario["id"] = fila_sql.id
        diccionario["comentario"] = fila_sql.comentario
        lista_comentarios.append(diccionario)

    resultado = {
        "id": libro.id,
        "titulo": libro.titulo,
        "fecha": libro.anho,
        "comentarios": lista_comentarios,
    }

    return JsonResponse(resultado, json_dumps_params={"ensure_ascii": False})

@csrf_exempt
def guardar_comentario(request, libro_id):
    if request.method != "POST":
        return None
    json_peticion = json.loads(request.body)
    comentario = Tcomentarios()
    comentario.comentario = json_peticion['nuevo_comentario']
    comentario.libro = Tlibros.objects.get(id=libro_id)
    comentario.save()
    return JsonResponse({"status":"ok"})
