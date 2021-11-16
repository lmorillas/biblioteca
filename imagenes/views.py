from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from imagenes.models import Imagen
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class ImagenesListView(ListView):
    model = Imagen
    template_name = 'imagenes/imagenes_list.html'
    context_object_name = 'imagenes'
    paginate_by = 10
    ordering = ['-fecha_subida']

class ImagenCreateView(SuccessMessageMixin, CreateView):
    model = Imagen
    fields = '__all__'
    template_name = 'imagenes/imagen_crear.html'

    success_url = '/imagenes'
    # form_class = AuthorForm
    success_message = "%(titulo)s se ha subido correctamente"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.subida_por = self.request.user
        return super().form_valid(form)

