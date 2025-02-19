from django.contrib import admin
from .models import Genre
from .models import Author
from .models import Book
from .models import Lenguaje
from .models import BookInstance
from .models import AuthorX
from .models import UserX
from .models import PublisherX
from django.contrib.auth.models import  Permission
from .models import BooksX
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Lenguaje)
admin.site.register(BookInstance)
admin.site.register(AuthorX)
admin.site.register(BooksX)
admin.site.register(UserX)
admin.site.register(PublisherX)
from .models import usuarioX
from .models import *
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)

admin.site.register(Permission)
admin.site.register(usuarioX)


admin.site.register(mensaje)
admin.site.register(votos)
admin.site.register(solicitud)
admin.site.register(Ejemplares_lectores)
admin.site.register(comentario)
