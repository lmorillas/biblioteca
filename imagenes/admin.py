from django.contrib import admin
from imagenes.models import Imagen
# Register your models here.

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    pass