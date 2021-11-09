from django.urls import include, path
from catalogo.views import LibrosListView, SearchResultsListView, \
    crear_autor



urlpatterns = [
    path('libros/', LibrosListView.as_view(), 
        name='listado_libros'),
    path('buscarlibros/', SearchResultsListView.as_view(),
        name="buscalibros" ),
    path('autor/create', crear_autor, name='crear_autor')
]