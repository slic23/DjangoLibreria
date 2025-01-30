from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

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
    path('calculo/<str:numero>',views.calcular,name="calculo"),
    path('operacion/<str:operador>', views.operacion,name="operacion") ,
    path('logout/', LogoutView.as_view(template_name='templates/registration/logged_out.html'), name='logout'),
    path('usuario/<str:nombre>',views.usuario,name="usuario"),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('crearAutor',views.autor, name="crearAutor")
]

urlpatterns += [
    path('create/', views.AuthorCreate.as_view(), name='author-create'),
    path('autores/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('autores/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]


