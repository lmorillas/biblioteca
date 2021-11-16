'''
0. Recuerda añadir app a intalled apps en settings.py
1. Definir modelos
2. python manage.py migrate

'''

from django.db import models
from django.db.models.base import Model

# Create your models here.
class Genre(models.Model):
    name = models.CharField("Género",max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

class Author(models.Model):
    first_name = models.CharField('Nombre', 
        max_length=100)
    last_name = models.CharField('Apellido', 
        max_length=100)
    date_of_birth = models.DateField('Fecha nacimiento', 
        null=True, blank=True)
    date_of_death = models.DateField('Fallecido', 
        null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Book(models.Model):
    '''
    Libro para aplicación de biblioteca ...
    '''
    title = models.CharField('Título', max_length=250)
    summary = models.TextField('Resumen', blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    fecha = models.DateField(blank=True, null=True,
        help_text='Fecha de publicación')

    # faltan relaciones
    author = models.ForeignKey('Author', on_delete=models.SET_NULL,
        null=True, verbose_name='Autor')
    genre = models.ManyToManyField(Genre, 
        verbose_name='Géneros')
    
    def __str__(self):
        return self.title

    def muestra_genero(self):
        '''Muestra género para admin'''
        return ', '.join([gen.name for gen in 
                    self.genre.all()[:2]])
    muestra_genero.short_description = 'Género'

    class Meta:
        verbose_name = 'Libro'


class Fotos(models.Model):
    titulo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="fotos/")