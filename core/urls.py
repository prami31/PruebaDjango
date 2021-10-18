from core import views
from django.urls import path, include

from rest_framework import routers

from core import api

router = routers.DefaultRouter()
router.register('autores', api.AutorViewSet)

app_name = 'core'


urlpatterns = [
    path('api/core/', include(router.urls)),
    path('autores/', views.autores),
    path('libros/ver/<int:autor_id>/', views.ver_libros, name="ver_libros"),
    path('autor/editar/<int:autor_id>/',
         views.editar_autor, name="editar_autor"),
    path('agregar/autor/', views.agregar_autor),
    path('agregar/eficaz/', views.agregar_autor_eficaz),
]
