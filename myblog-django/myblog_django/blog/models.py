from distutils.command.upload import upload
from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
#con verbose_name podemos especificar el nombre como se vera en el admin page, ejemp. image = models.ImageField(verbose_name='Imagen')
class Post(models.Model):
    image = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=200)
    desc = models.TextField()
    cotent = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    #Aqui podemos especificar en singular y plural como queremos que se llame el metodo (Post en este caso)
    #class Meta:
    #verbose_name = 'Publicacion'
    #verbose_name_plural = 'publicaciones'

    def __str__(self):
        return self.title
    
