from django.shortcuts import render, redirect
from catalogo.models import Book, Author
from django.views import generic
from django.urls import resolve, reverse
from django.views.generic import ListView
from catalogo.forms import AuthorForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# from django.http import HttpResponse

# Create your views here.
# vistas tipo función

def indice(request):
    '''
    Página inicial de nuerear_autostra web
    '''
    datos = {'autor': 'Luis Miguel'}
    # ejemplo sesiones
    visitas = request.session.get('visitas', 0)
    request.session['visitas'] = visitas + 1
    datos['visitas'] = visitas

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
            # Mensaje para informar éxito redirección
            messages.add_message(request, 
                messages.SUCCESS, 
                'Autor creado.')
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

class AutoresListView(generic.ListView):
    '''
    Vista genérica para nuestro listado de autores
    '''
    model = Author
    paginate_by = 15
    queryset = Author.objects.all().order_by('last_name', 'first_name')


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

# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class CrearAutor(SuccessMessageMixin, generic.CreateView):
    model = Author
    #fields = '__all__'
    template_name = 'crear_autor.html'
    success_url = '/'
    form_class = AuthorForm
    success_message = "%(first_name)s %(last_name)s se ha creado correctamente"


# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class ModificarAutor(SuccessMessageMixin, generic.UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'modificar_autor.html'
    success_url = '/'
    success_message = "%(first_name)s %(last_name)s se ha modificado correctamente"


# Creación de autor con CreateView. Añadimos SuccessMesaageMixin para mensaje de éxito.
class EliminarAutor(generic.DeleteView):
    model = Author
    success_url = '/catalago/autores' #reverse('listado_autores')
    success_message = "El autor se ha borrado correctamente"
    template_name = 'autor_confirmar_borrado.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarAutor, self).delete(
            request, *args, **kwargs)
