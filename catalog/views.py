from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views  import generic
from catalog.models import *
from django.db.models import Sum
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
    
    num_visits = request.session.get('visitas', 0)
    num_visits += 1
    request.session['visitas'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
def ListarLibros(request):
    numLibros =  Book.objects.all()
    context = {
	'numlibros':numLibros
    }
    
    return render(request,'libros.html' , context)

def VistaDetalle(request,pk):
    Libro = Book.objects.filter(pk=pk)[0]
    context = { 'Libro':Libro}

    return render(request,'detalle.html',context)
def index2(request, numero1):
     if numero1 != 0:
        Libro = Book.objects.filter(pk=numero1)[0]
        autor = Author.objects.get(pk=Libro.author.pk)
        dictautor = {'nombreAutor': autor.first_name}
        datos1= {
            'titulo': Libro.title,
            'lenguaje': Libro.lenguaje,
            'sinopsis': Libro.summary,
            'isbn': Libro.isbn,
            'autor': dictautor
        }
        return JsonResponse(datos1)

     else:
         libros = list(Book.objects.all())
         paquete = []
         for libro in libros:
             autor = Author.objects.filter(pk=libro.author.pk)[0]
             dictautor = {'nombreAutor':autor.first_name}
             datos2 = {
                 'titulo':libro.title,
                 'autores':dictautor
             }
             
	
             paquete.append(datos2)
         return JsonResponse({'paquete':paquete})
         
	     

   
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    orphans = 0
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all() # Get 5 books containing the title war
    template_name = 'book_list.html'  # Specify your own template name/location


def devolver(request):
    valor1 =  request.GET["valor"]
    valor2 = request.GET["valor2"]
    mensaje = f'Este es el mensaje {valor1} y valor dos es {valor2}'
    return HttpResponse(mensaje)
  
def consultas(request):
    autores_escor = list(AuthorX.objects.filter( popularity_score__gte = 7).values_list('pk',flat=True))
    """

lista = []
    for i in autores_escor:
        
        lista.append(i['pk'])
        
    print(lista)
    """
    
''''''''
   # return HttpResponse(libros)
"""
 def listing(request):
    contact_list = Books.objects.all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})

"""




def probandoSession(request):
    pass
