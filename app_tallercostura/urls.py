
from django.urls import path

from . import views



urlpatterns = [

    path('', views.inicio_tallercostura, name='inicio_tallercostura'),
    path('alumno/', views.ver_alumno, name='ver_alumno'),

    path('alumno/agregar/', views.agregar_alumno, name='agregar_alumno'),

    path('alumno/actualizar/<int:id>/', views.actualizar_alumno, name='actualizar_alumno'),

    path('alumno/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_alumno, name='realizar_actualizacion_alumno'),

    path('alumno/borrar/<int:id>/', views.borrar_alumno, name='borrar_alumno'),
    
    #clase 
    path('clases/', views.ver_clase, name='ver_clase'),
    path('clases/agregar/', views.agregar_clase, name='agregar_clase'),
    path('clases/actualizar/<int:id>/', views.actualizar_clase, name='actualizar_clase'),
    path('clases/borrar/<int:id>/', views.borrar_clase, name='borrar_clase'),

    #inscripcion

    path('inscripcion/', views.ver_inscripcion, name='ver_inscripcion'),
    path('inscripcion/agregar/', views.agregar_inscripcion, name='agregar_inscripcion'),
    path('inscripcion/actualizar/<int:pk>/', views.actualizar_inscripcion, name='actualizar_inscripcion'),
    path('inscripcion/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_inscripcion, name='realizar_actualizacion_inscripcion'),
    path('inscripcion/borrar/<int:pk>/', views.borrar_inscripcion, name='borrar_inscripcion'),
      

      #profesor 

       # --- Material ---
    path('material/agregar/', views.agregar_material, name='agregar_material'),
    path('material/ver/', views.ver_material, name='ver_material'),
    path('material/actualizar/<int:pk>/', views.actualizar_material, name='actualizar_material'),
    path('material/realizar_actualizacion/guardar/<int:pk>/', views.realizar_actualizacion_material, name='realizar_actualizacion_material'),
    path('material/borrar/<int:pk>/', views.borrar_material, name='borrar_material'),

    # --- Profesor (si lo tienes) ---
    path('profesor/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesor/ver/', views.ver_profesor, name='ver_profesor'),
    path('profesor/actualizar/<int:pk>/', views.actualizar_profesor, name='actualizar_profesor'),
    path('profesor/realizar_actualizacion/guardar/<int:pk>/', views.realizar_actualizacion_profesor, name='realizar_actualizacion_profesor'),
    path('profesor/borrar/<int:pk>/', views.borrar_profesor, name='borrar_profesor'),

]



