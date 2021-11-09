from django.shortcuts import render, redirect
from catalogo.models import Book
from django.views import generic
from django.views.generic import ListView
from catalogo.forms import AuthorForm
from django.contrib import messages


# from django.http import HttpResponse

# Create your views here.
# vistas tipo función

def indice(request):
    '''
    Página inicial de nuestra web
    '''
    datos = {'autor': 'Luis Miguel'}
    
    # últimos 5 libros del catálogo
    libros = Book.objects.all().order_by('-id')[:5]

    datos['libros'] = libros

    return render(request, 'index.html',
        context=datos)

def todos_libros(request):
    libros = Book.objects.all().order_by('title')
    return render(request, 'todos_libros.html',
        context={'libros': libros})

# Creación de autor
def crear_autor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Autor creado.')
            return redirect('/')
    else:
        form = AuthorForm()
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
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(title__icontains=query)
        return []  # cuando entramos a buscar o si no se introduce nada
