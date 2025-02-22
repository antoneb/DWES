"""
URL configuration for segundo_trimestre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from webserviceapp import views
from rest_framework.authtoken.views import ObtainAuthToken
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from webserviceapp.views import (ListarEventosAPIView, InfoEventoIndividualAPIView, CrearEventoAPIView, ActualizarEventoAPIView, EliminarEventoAPIView)
from webserviceapp.views import (ListarReservasAPIView, CrearReservaAPIView, ActualizarReservaAPIView,EliminarReservaAPIView)
from webserviceapp.views import (ListarComentariosEventoAPIView,GuardarComentarioAPIView,LoginUsuarioAPIView,CrearUsuarioAPIView)

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentación",
        default_version="v1",
        description="Documentación de la API",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    # APIView
    path('eventos/', views.ListarEventosAPIView.as_view(), name='listar_eventos'),
    path('eventos/<int:id>/', views.InfoEventoIndividualAPIView.as_view(), name='info_evento_individual'),
    path('crear_evento', views.CrearEventoAPIView.as_view(), name='crear_evento'),
    path('actualizar_evento/<int:id>', views.ActualizarEventoAPIView.as_view(), name='actualizar_evento'),
    path('eliminar_evento/<int:id>', views.EliminarEventoAPIView.as_view(), name='eliminar_evento'),

    path('listar_reservas/<int:id>', views.ListarReservasAPIView.as_view(), name='listar_reservas'),
    path('crear_reserva', views.CrearReservaAPIView.as_view(), name='crear_reserva'),
    path('actualizar_reserva/<int:id>', views.ActualizarReservaAPIView.as_view(), name='actualizar_reserva'),
    path('eliminar_reserva/<int:id>', views.EliminarReservaAPIView.as_view(), name='eliminar_reserva'),

    path("listar_comentarios_evento/<int:id>", views.ListarComentariosEventoAPIView.as_view(),name='listar_comentarios_evento'),
    path("guardar_comentario/<int:id>", views.GuardarComentarioAPIView.as_view(), name='guardar_comentario'),

    path("login_usuario", views.LoginUsuarioAPIView.as_view(), name='login_usuario'),
    path("crear_usuario", views.CrearUsuarioAPIView.as_view(), name='crear_usuario'),

]
