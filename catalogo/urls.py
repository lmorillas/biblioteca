from django.urls import include, path
from catalogo.views import LibrosListView, SearchResultsListView, \
    crear_autor, CrearAutor



urlpatterns = [
    path('libros/', LibrosListView.as_view(), 
        name='listado_libros'),
    path('buscarlibros/', SearchResultsListView.as_view(),
        name="buscalibros" ),
    path('autor/crear', crear_autor, name='crear_autor'),
    path('autor/crear2', CrearAutor.as_view(), name='crear_autor2'),
]