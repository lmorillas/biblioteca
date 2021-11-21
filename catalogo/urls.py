from django.urls import include, path
from catalogo.views import LibrosListView, SearchResultsListView, \
    crear_autor, CrearAutor, ModificarAutor, EliminarAutor, AutoresListView,\
    subir_archivo, mapa



urlpatterns = [
    path('libros/', LibrosListView.as_view(), 
        name='listado_libros'),
    path('buscarlibros/', SearchResultsListView.as_view(),
        name="buscalibros" ),
    path('autores/', AutoresListView.as_view(), 
        name='listado_autores'),
    path('autor/crear', crear_autor, name='crear_autor'),
    path('autor/crear2', CrearAutor.as_view(), name='crear_autor2'),
    path('autor/modificar/<int:pk>', ModificarAutor.as_view(), name='modificar_autor'),
    path('autor/eliminar/<int:pk>', EliminarAutor.as_view(), name='eliminar_autor'),
    path('subir-archivo', subir_archivo, name='subir-archivo'),
    path('mapa', mapa, name='mapa'),
]