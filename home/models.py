from django.db import models


# Create your models here.
class Estudiante(models.Model):
    doc = (
        ('D','Matematicas'),
        ('C','DesarrolloWeb'),

    )
    
    nombre =models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    direccion =models.CharField(max_length=200)
    nacimiento = models.DateField()
    tipo = models.ForeignKey(
        'ListadoEstudiantes',
        on_delete= models.CASCADE,
        default=1
        )
    documento = models.CharField(
        max_length=20,
        choices=doc,
        default='C')
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)




class Administradores(models.Model):
    
    nombre =models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    direccion =models.CharField(max_length=200)
    nacimiento = models.DateField()
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)






class ListadoEstudiantes(models.Model):
    tipo = models.CharField(max_length=10)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '%s' % (self.tipo)


class Cursos(models.Model):
    curso = models.ManyToManyField(Estudiante)
    fecha = models.DateTimeField()


class Catedraticos(models.Model):
    doc = (
        ('D','DPI'),
        ('C','CEDULA'),

    )
    nombre =models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    direccion =models.CharField(max_length=200)
    documento = models.CharField(
        max_length=20,
        choices=doc,
        default='C')
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)