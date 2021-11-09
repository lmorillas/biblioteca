from django.shortcuts import render
from catalogo.models import Book
from django.views import generic


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

class LibrosListView(generic.ListView):
    '''
    Vista genérica para nuestro listado de libros
    '''
    model = Book
    paginate_by = 15

