from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    nomenclatura = models.CharField(max_length=5)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta():
        verbose_name_plural = "Paises"


class Departamento(models.Model):
    nombre = models.CharField(max_length=250)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL,null=True)#ForeignKey 1 a 1
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta():
        verbose_name_plural = "Departamentos"


class Ciudad(models.Model):
    nombre = models.CharField(max_length=250)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL,null=True)#ForeignKey 1 a 1
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True,blank=True) 

    def __str__(self):
        return self.nombre

    class Meta():
        verbose_name_plural = "Ciudades"
    

class Barrio(models.Model):
    nombre = models.CharField(max_length=250)
    complemento = models.CharField(max_length=250,null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True,blank=True)#ForeignKey 1 a 1
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True,blank=True) 

    def __str__(self):
        return self.nombre

    class Meta():
        verbose_name_plural = "Barrio"