from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('libritos/', views.ListarLibros,name="ListarLibros"),
    path('libritos/<int:pk>', views.VistaDetalle, name='book-detail'),
    path('<int:numero1>/',views.index2,name='index2')
]
