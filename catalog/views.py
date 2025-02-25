from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views  import generic
from catalog.models import *
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import TodoSerializer




import datetime

from .forms import RenewBookForm
from .models import Book, Author, BookInstance, Genre

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author
from django.contrib import messages
import os 
from fpdf import FPDF
#@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    #generando pdf con el modelo book de un libro en particular 
    #primero chequeo de que si existe ese pdf no volver a generarlo 
    libro = Book.objects.filter(title="Guerra y Paz")[0]
    if not os.path.exists('catalog/static/libro.pdf'):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40, 10, libro.title )
        pdf.cell(10, 20, libro.summary)
        pdf.add_page()
        pdf.image(libro.portada.path, x=90, y=20, w=100)
        pdf.output('catalog/static/libro.pdf', 'F')

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
    
    
    messages.add_message(request, messages.SUCCESS, 'Estas dentro de index')
    

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
def ListarLibros(request):
    numLibros =  Book.objects.all()
    context = {
	'numlibros':numLibros
    }
    
    return render(request,'libros.html' , context)

def VistaDetalle(request,pk):
    Libro = get_object_or_404(Book, pk=pk)
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

def todosAutores(request):
    autores = Author.objects.all()
    contexto = {
        'numAutores':autores
    }
    return render(request,"todosAutores.html",contexto)
from django.contrib.auth.decorators import permission_required,login_required

@permission_required('catalog.calculadoraAcceso')
def calculadora(request):
    #return render(request,'calculadora.html',{})
     return render(request,'calculadora.html',{})
 
def calcular(request, numero):
    primerNumero = request.session.get('primerNumero', 0)
    operacion = request.session.get('operacion', '')
    siguienteNumero = request.session.get('siguienteNumero', 0)

    contexto = {'id': 0}
    request.session['primerNumero'] = numero
    request.session['siguienteNumero'] = primerNumero

    if operacion == 'suma':
        contexto['id'] = int(request.session['primerNumero']) + int(request.session['siguienteNumero'])
        return render(request, 'calculadora.html', contexto)
    elif operacion == 'resta':
        contexto['id'] = int(request.session['primerNumero']) - int(request.session['siguienteNumero'])
        return render(request, 'calculadora.html', contexto)
    elif operacion == 'multiplicacion':
        contexto['id'] = int(request.session['primerNumero']) * int(request.session['siguienteNumero'])
        return render(request, 'calculadora.html', contexto)
    elif operacion == 'division':
        contexto['id'] = int(request.session['primerNumero']) / int(request.session['siguienteNumero'])
        return render(request, 'calculadora.html', contexto)

    return render(request, 'calculadora.html', contexto)

def operacion(request, operador):
    request.session['operacion'] = operador
    return render(request, 'calculadora.html', {})
import re 
def calculoEcuacion(request):
    pass


def usuario(request,nombre):
    usarioB = User.objects.create_user(username = nombre, password = "issam23")
    userA = usuarioX.objects.create(user = usarioB, username = nombre, email = f"{nombre}@gmail.com")
    return HttpResponse(f'El usuario {userA.username} ha sido creado')
    

def renew_book_librarian(request, pk):
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()
            messages.add_message(request, messages.SUCCESS, 'El libro ha sido añadido')
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})

from .forms import CrearAutor
from .forms import addLibro
def autor(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CrearAutor(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CrearAutor(request.GET)

    return render(request, "crear_autor.html", {"form": form})

def crearLibro(request):
    if request.method == "POST":
        form = addLibro(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['title']
            lenguaje = form.cleaned_data['lenguaje']
            autor = form.cleaned_data['author']
            sinopsis = form.cleaned_data['summary']
            isb = form.cleaned_data['isbn']
            portada = form.cleaned_data['portada']
            genero = form.cleaned_data['genre']
            
            libro = Book(title=titulo, lenguaje= lenguaje,author= autor,summary = sinopsis,isbn = isb  )
            libro.save()
            libro.genre.set([genero][0])
            messages.add_message(request, messages.SUCCESS, 'El libro ha sido añadido ')

            return render(request,'index.html',{})

    else:
        form= addLibro(request.GET)
    return render(request,'addlibro.html',{"form":form})

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'05/01/2018',}
    success_url = reverse_lazy('autores')

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']
    success_url = reverse_lazy('autores')
class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('autores')




def generarDatos(request):
    pass




class TodoListApiView(APIView):
    # add permission to check if user is authenticated
   

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = Book.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class addLibro(CreateView):
 
    model = Book
    success_url= reverse_lazy('books')
    
    fields = ('__all__')



@login_required
def accesoLector(request):
    usuario_actual = request.user
 
    usuarioF = usuarioX.objects.filter(username = request.user)[0]
    lista = solicitud.objects.filter(solicitante = usuarioF.pk)

    
    
    return render(request, 'lector.html', {'lector': usuarioF,"lista":lista})


def mensajes(request,pk):
    usarioF = solicitud.objects.filter(pk=pk)[0]
    remitente = usarioF.solicitante.username
    recibe = usarioF.destinatario.username
    mensajes = mensaje.objects.filter(remitente__username= remitente)
    contexto = {
        "remitente":remitente,
        "recibe":recibe,
        "mensajes":mensajes,
        "usuario":usarioF
    }
    
    return render(request,'mensajes.html', contexto)
