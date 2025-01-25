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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path("prueba", views.pagina_de_prueba),
    path("listar_eventos", views.listar_eventos),
    path('eventos/<int:id>/', views.info_evento_individual),
    path('crear_evento', views.crear_evento),
    path('actualizar_evento/<int:id>', views.actualizar_evento),
    path('eliminar_evento/<int:id>', views.eliminar_evento),

    path('listar_reservas/<int:id>', views.listar_reservas),
    path('crear_reserva', views.crear_reserva),
    path('actualizar_reserva/<int:id>', views.actualizar_reserva),
    path('eliminar_reserva/<int:id>', views.eliminar_reserva),

    path("listar_comentarios_evento/<int:id>", views.listar_comentarios_evento),
    path("guardar_comentario/<int:id>", views.guardar_comentario),

    path("login_usuario", views.login_usuario),
]
