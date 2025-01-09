from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('libritos/', views.ListarLibros,name="ListarLibros"),
    path('libritos/<int:pk>', views.VistaDetalle, name='book-detail'),
    path('<int:numero1>/',views.index2,name='index2'),
    path('libros/',views.BookListView.as_view(),name="books"),
    path('mostrar/',views.devolver,name='devolver'),
    path('consultas/',views.consultas, name="consultas"),
    path('autores/',views.todosAutores,name="autores"),
    path('calculadora/',views.calculadora,name="calculadora"),
    path('calculo/<int:id>',views.calcular,name="calculo")
]
