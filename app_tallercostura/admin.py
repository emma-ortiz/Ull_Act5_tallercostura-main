
from django.contrib import admin

from .models import Alumno, Clase, Inscripcion, Profesor, Material


admin.site.register(Alumno)

admin.site.register(Clase)

admin.site.register(Inscripcion)

admin.site.register(Profesor)

admin.site.register(Material)
