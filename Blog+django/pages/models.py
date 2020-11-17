from django.db import models

""" texto enriquecido """
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    #content = models.TextField(verbose_name='Contenido')
    slug = models.CharField(max_length=150, unique=True,
    verbose_name='URL amigable')
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True,
    verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now_add=True, 
    verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return f'{self.title}'

"""  Agregar el feature de text enriquecido  
    
    o Ajustar content = models.RichTextField(....)

"""