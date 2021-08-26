from django.contrib.admin import autodiscover
from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural  = 'Autores'
        ordering = ['nombres','nacionalidad']

    def __str__(self) -> str:
        return self.nombres

class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha Publicacion', blank=False, null=False)
    autor_id = models.ManyToManyField(Autor)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural  = 'Libros'
        ordering = ['titulo','fecha_publicacion']
    
    def __str__(self) -> str:
        return self.titulo
