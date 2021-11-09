from django.shortcuts import render
from catalogo.models import Book
from django.views import generic
from django.views.generic import ListView
from catalogo.forms import AuthorForm

# from django.http import HttpResponse

# Create your views here.
# vistas tipo función

def indice(request):
    '''
    Página inicial de nuestra web
    '''
    datos = {'autor': 'Luis Miguel'}
    
    
    busqueda = request.GET.get('q')
    if busqueda:
        libros = Book.objects.filter(
            title__icontains=busqueda)
        datos['noencontrado'] = True
    else:
        libros = Book.objects.all()
        
    datos['libros'] = libros

    
    return render(request, 'index.html',
        context=datos)

def todos_libros(request):
    libros = Book.objects.all().order_by('title')
    return render(request, 'todos_libros.html',
        context={'libros': libros})

# Creación de autor
def crear_autor(request):
    datos = {'form': AuthorForm()}
    return render(request, 'crear_autor.html', 
        context=datos)



class LibrosListView(generic.ListView):
    '''
    Vista genérica para nuestro listado de libros
    '''
    model = Book
    paginate_by = 15


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'libros'
    template_name = 'search_results.html'  # No usará la plantilla estándar del ListView

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(title__icontains=query)
        else: 
            return Book.objects.all()
