from django.urls import path
from . import views 
from catalog import views

urlpatterns = [
    path('listaLibros', views.TodoListApiView.as_view()),
]