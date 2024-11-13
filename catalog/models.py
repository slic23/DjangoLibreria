from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
# Create your models here.
class Genre(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.name

class Author(models.Model):
    """
    Modelo que representa un autor
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)
   
class Book(models.Model):
    """
    Modelo que representa un libro (pero no un Ejemplar específico).
    """
    
    title = models.CharField(max_length=200)
    lenguaje  = models.ForeignKey('Lenguaje', on_delete=models.CASCADE,null=True) 
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.

    summary = models.TextField(max_length=1000, help_text="Ingrese una breve descripción del libro")

    isbn = models.CharField('ISBN',max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField(Genre, help_text="Seleccione un genero para este libro")
    # ManyToManyField, porque un género puede contener muchos libros y un libro puede cubrir varios géneros.
    # La clase Genre ya ha sido definida, entonces podemos especificar el objeto arriba.

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.title


    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'
   


class Lenguaje(models.Model):
	lenguage =  models.CharField(max_length=100,default="español")
	def __str__(self):
	   return self.lenguage
class BookInstance(models.Model):

    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'
class AuthorX(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True , blank=True)
    zipcode = models.IntegerField(null=True)
    telephone = models.CharField(max_length=100, null=True)
    recommendedby = models.ForeignKey('AuthorX', on_delete=models.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', null=True,blank=True)
    joindate = models.DateField()
    popularity_score = models.IntegerField()
    followers = models.ManyToManyField('UserX', related_name='followed_authors',related_query_name='followed_authors')
    def __str__(self):
         return self.firstname + ' ' + self.lastname
class PublisherX(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	recommendedby = models.ForeignKey('PublisherX', on_delete=models.CASCADE, null=True ,blank=True)
	joindate = models.DateField()
	popularity_score = models.IntegerField()
	def __str__(self):
	    return self.firstname + ' ' + self.lastname

class BooksX(models.Model):
	title = models.CharField(max_length=100)
	genre = models.CharField(max_length=200)
	price = models.IntegerField(null=True)
	published_date = models.DateField()
	author = models.ForeignKey('AuthorX', on_delete=models.CASCADE, related_name='books', related_query_name='books')
	publisher = models.ForeignKey('PublisherX', on_delete=models.CASCADE, related_name='books', related_query_name='books')
	def __str__(self):
            return self.title
     
class UserX(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
	    return  self.username

# escriba una consulta , el  titulo , fecha de publicacion , 

