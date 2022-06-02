from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Name', max_length= 100)
    apellido = models.CharField('Last name', max_length= 200)

    def __str__(self):
        return f'{self.apellido},{self.nombre}'