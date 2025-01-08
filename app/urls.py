from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mostrar/', views.mostrar, name='mostrar'),
    path('editar/', views.editar, name='editar'),
    path('ingresar/', views.ingresar, name='ingresar'),
    path('eliminar/', views.eliminar, name='eliminar'),
]
