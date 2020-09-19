from django.contrib import admin
from .models import Estudiante,Administradores,ListadoEstudiantes,Cursos,Catedraticos

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Administradores)
admin.site.register(ListadoEstudiantes)
admin.site.register(Cursos)
admin.site.register(Catedraticos)