from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
def ListarLibros(request):
    numLibros =  Book.objects.all()
    context = {
	'numlibros':numLibros
    }
    return render(request,'index.html' , context= context)

def VistaDetalle(request,pk):
    Libro = Book.objects.filter(pk=pk)[0]
    context = { 'Libro':Libro}
    return HttpResponse(Libro.author)
def index2(request, numero1):
    if numero1 == 0:
        Libro = Book.objects.filter(pk=numero1)[0]
        autor = Author.objects.get(pk=Libro.author.pk)
        #dictautor = {'nombreAutor': autor.first_name}
        datos1= {
            'titulo': Libro.title,
            'lenguaje': Libro.lenguaje,
            'sinopsis': Libro.summary,
            'isbn': Libro.isbn,
           # 'autor': dictautor
        }
        return JsonResponse(datos)
    else:
        libros = Book.objects.all()
        paquete = []
        for libro in libros:
            #autor = Author.objects.filter(pk=libro.author.pk)[0]
            #dictautor = {'nombreAutor': autor.first_name}
            datos2 = {
            'titulo': libro.title,
            #'lenguaje': libro.lenguaje,
            'sinopsis': libro.summary,
            'isbn': libro.isbn,
            #'autor': dictautor
        }
            
            paquete.append(datos2)
        return JsonResponse(paquete )
