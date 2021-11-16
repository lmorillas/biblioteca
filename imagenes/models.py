from django.db import models
from django.conf import settings


def get_upload_to(instancia, filename):
    return instancia.get_upload_to(filename)

# Create your models here.
class Imagen(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='título')
    file = models.ImageField(upload_to="imagenes/%Y/%m/%d/", verbose_name='imagen',
        height_field= 'alto', width_field='ancho')
    
    ancho = models.IntegerField(editable=False, default=0)
    alto = models.IntegerField(editable=False, default=0)
    fecha_subida = models.DateTimeField(verbose_name='Fecha de subida', auto_now_add=True,
        db_index=True, blank=True, null=True)
    subida_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Subida por usuario',
        null=True, blank=True, editable=False, 
        on_delete=models.SET_NULL
    )
    

    def __str__(self):
        return self.titulo