from django.urls import include, path
from imagenes.views import *


urlpatterns = [
    path('', ImagenesListView.as_view(), 
        name='catalogo'),
    path('crear', ImagenCreateView.as_view(),
        name="creaimagen" ),
    
]