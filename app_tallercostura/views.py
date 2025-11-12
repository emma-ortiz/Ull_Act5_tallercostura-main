
from django.shortcuts import render, redirect, get_object_or_404

from .models import Alumno
from django.urls import reverse
from django.utils import timezone
from decimal import Decimal
from .models import Clase, Profesor
from .models import Inscripcion
from .models import Profesor
from .models import Material 



def inicio_tallercostura(request):

    return render(request, 'inicio.html')



def agregar_alumno(request):

    if request.method == 'POST':

        nombre = request.POST['nombre']

        apellido = request.POST['apellido']

        correo = request.POST['correo']

        telefono = request.POST['telefono']

        direccion = request.POST['direccion']

        fecha_nacimiento = request.POST['fecha_nacimiento']

        Alumno.objects.create(

            nombre=nombre,

            apellido=apellido,

            correo=correo,

            telefono=telefono,

            direccion=direccion,

            fecha_nacimiento=fecha_nacimiento

        )

        return redirect('ver_alumno')

    return render(request, 'alumno/agregar_alumno.html')



def ver_alumno(request):

    alumnos = Alumno.objects.all()

    return render(request, 'alumno/ver_alumno.html', {'alumnos': alumnos})



def actualizar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    return render(request, 'alumno/actualizar_alumno.html', {'alumno': alumno})

# 👉 Procesar el envío del formulario y actualizar en la base de datos
def realizar_actualizacion_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)

    if request.method == 'POST':
        alumno.nombre = request.POST.get('nombre')
        alumno.apellido = request.POST.get('apellido')
        alumno.correo = request.POST.get('correo')
        alumno.telefono = request.POST.get('telefono')
        alumno.direccion = request.POST.get('direccion')
        alumno.fecha_nacimiento = request.POST.get('fecha_nacimiento')

        # ✅ NO modificar fecha_registro, se deja igual
        alumno.save()

        return redirect('ver_alumno')

    # Si entra por GET, redirige al formulario de nuevo
    return render(request, 'alumno/actualizar_alumno.html', {'alumno': alumno})


def borrar_alumno(request, id):

    alumno = get_object_or_404(Alumno, id=id)

    if request.method == 'POST':

        alumno.delete()

        return redirect('ver_alumno')

    return render(request, 'alumno/borrar_alumno.html', {'alumno': alumno})
        
        #clase 

from django.shortcuts import render, redirect, get_object_or_404
from .models import Clase

# 🧾 Ver lista de clases
def ver_clase(request):
    clases = Clase.objects.all()
    return render(request, 'clase/ver_clase.html', {'clases': clases})

# ➕ Agregar nueva clase
def agregar_clase(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        nivel = request.POST.get('nivel')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        duracion_horas = request.POST.get('duracion_horas')
        cupo_maximo = request.POST.get('cupo_maximo')
        profesor_id = request.POST.get('profesor')

        clase_kwargs = dict(
            nombre=nombre,
            descripcion=descripcion,
            nivel=nivel,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            duracion_horas=duracion_horas,
            cupo_maximo=cupo_maximo
        )

        # asignar profesor si viene seleccionado
        if profesor_id:
            try:
                prof = Profesor.objects.get(pk=int(profesor_id))
                clase_kwargs['profesor'] = prof
            except (Profesor.DoesNotExist, ValueError):
                pass

        Clase.objects.create(**clase_kwargs)
        return redirect('ver_clase')

    profesores = Profesor.objects.all().order_by('apellido', 'nombre')
    return render(request, 'clase/agregar_clase.html', {'profesores': profesores})

# ✏️ Actualizar clase
def actualizar_clase(request, id):
    clase = get_object_or_404(Clase, id=id)
    if request.method == 'POST':
        clase.nombre = request.POST.get('nombre')
        clase.descripcion = request.POST.get('descripcion')
        clase.nivel = request.POST.get('nivel')
        clase.fecha_inicio = request.POST.get('fecha_inicio')
        clase.fecha_fin = request.POST.get('fecha_fin')
        clase.duracion_horas = request.POST.get('duracion_horas')
        clase.cupo_maximo = request.POST.get('cupo_maximo')
        clase.save()
        return redirect('ver_clase')
    return render(request, 'clase/actualizar_clase.html', {'clase': clase})

# ❌ Borrar clase
def borrar_clase(request, id):
    clase = get_object_or_404(Clase, id=id)
    clase.delete()
    return redirect('ver_clase')

#views para inscripcion 

def agregar_inscripcion(request):
        if request.method == 'POST':
            alumno_id = request.POST.get('alumno')
            clase_id = request.POST.get('clase')
        metodo_pago = request.POST.get('metodo_pago')
        monto_pagado = request.POST.get('monto_pagado')
        estado = request.POST.get('estado')
        observaciones = request.POST.get('observaciones')


        alumno = get_object_or_404(Alumno, id=alumno_id)
        clase = get_object_or_404(Clase, id=clase_id)


        Inscripcion.objects.create(
        alumno=alumno,
        clase=clase,
        metodo_pago=metodo_pago,
        monto_pagado=monto_pagado,
        estado=estado,
observaciones=observaciones
)
        return redirect('ver_inscripcion')


# GET -> mostrar formulario con combos
def agregar_inscripcion(request):
    if request.method == 'POST':
        alumno_id = request.POST.get('alumno')
        clase_id = request.POST.get('clase')
        metodo_pago = request.POST.get('metodo_pago')
        monto_pagado = request.POST.get('monto_pagado')
        estado = request.POST.get('estado')
        observaciones = request.POST.get('observaciones')

        alumno = get_object_or_404(Alumno, id=alumno_id)
        clase = get_object_or_404(Clase, id=clase_id)

        Inscripcion.objects.create(
            alumno=alumno,
            clase=clase,
            metodo_pago=metodo_pago,
            monto_pagado=monto_pagado,
            estado=estado,
            observaciones=observaciones
        )
        return redirect('ver_inscripcion')

    # GET -> mostrar formulario con combos
    alumnos = Alumno.objects.all().order_by('nombre', 'apellido')
    clases = Clase.objects.all().order_by('nombre')
    return render(request, 'inscripcion/agregar_inscripcion.html', {'alumnos': alumnos, 'clases': clases})




# Ver todas las inscripciones (tabla)
def ver_inscripcion(request):
    inscripciones = Inscripcion.objects.select_related('alumno', 'clase').all().order_by('-fecha_inscripcion')
    return render(request, 'inscripcion/ver_inscripcion.html', {'inscripciones': inscripciones})




# Mostrar formulario para actualizar (seleccionado por id)
def actualizar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, id=pk)
    alumnos = Alumno.objects.all().order_by('nombre', 'apellido')
    clases = Clase.objects.all().order_by('nombre')
    return render(request, 'inscripcion/actualizar_inscripcion.html', {'inscripcion': inscripcion, 'alumnos': alumnos, 'clases': clases})




# Procesar actualización
def realizar_actualizacion_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, id=pk)
    if request.method == 'POST':
        alumno_id = request.POST.get('alumno')
        clase_id = request.POST.get('clase')
        inscripcion.metodo_pago = request.POST.get('metodo_pago')
        inscripcion.monto_pagado = request.POST.get('monto_pagado')
        inscripcion.estado = request.POST.get('estado')
        inscripcion.observaciones = request.POST.get('observaciones')

        # actualizar relaciones
        inscripcion.alumno = get_object_or_404(Alumno, id=alumno_id)
        inscripcion.clase = get_object_or_404(Clase, id=clase_id)

        inscripcion.save()
        return redirect('ver_inscripcion')

    return render(request, 'inscripcion/actualizar_inscripcion.html', {'inscripcion': inscripcion})




# Borrar inscripción (confirmación + POST)
def borrar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, id=pk)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('ver_inscripcion')
    return render(request, 'inscripcion/borrar_inscripcion.html', {'inscripcion': inscripcion})



# -------------------------
# PROFESOR - CRUD
# -------------------------

def ver_profesor(request):
    profesores = Profesor.objects.all().order_by('apellido', 'nombre')
    return render(request, 'profesor/ver_profesor.html', {'profesores': profesores})

def agregar_profesor(request):
    clases = Clase.objects.all().order_by('nombre')
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        apellido = request.POST.get('apellido', '')
        correo = request.POST.get('correo', '')
        telefono = request.POST.get('telefono', '')
        especialidad = request.POST.get('especialidad', '')
        fecha_contratacion = request.POST.get('fecha_contratacion', None)
        salario_raw = request.POST.get('salario', '0')
        try:
            salario = Decimal(salario_raw)
        except:
            salario = Decimal('0.00')

        prof = Profesor.objects.create(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            telefono=telefono,
            especialidad=especialidad,
            fecha_contratacion=fecha_contratacion,
            salario=salario
        )

        # asignar clases seleccionadas (multi select)
        clases_ids = request.POST.getlist('clases')  # [] si none
        if clases_ids:
            for cid in clases_ids:
                try:
                    c = Clase.objects.get(pk=int(cid))
                    c.profesor = prof
                    c.save()
                except Clase.DoesNotExist:
                    continue

        return redirect('ver_profesor')

    return render(request, 'profesor/agregar_profesor.html', {'clases': clases})


def actualizar_profesor(request, pk):
    prof = get_object_or_404(Profesor, pk=pk)
    clases = Clase.objects.all().order_by('nombre')
    # clases actualmente asignadas a este profesor
    clases_asignadas = Clase.objects.filter(profesor=prof).values_list('pk', flat=True)
    return render(request, 'profesor/actualizar_profesor.html', {
        'profesor': prof,
        'clases': clases,
        'clases_asignadas': list(clases_asignadas),
    })


def realizar_actualizacion_profesor(request, pk):
    prof = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        prof.nombre = request.POST.get('nombre', prof.nombre)
        prof.apellido = request.POST.get('apellido', prof.apellido)
        prof.correo = request.POST.get('correo', prof.correo)
        prof.telefono = request.POST.get('telefono', prof.telefono)
        prof.especialidad = request.POST.get('especialidad', prof.especialidad)
        fecha_contratacion = request.POST.get('fecha_contratacion', None)
        if fecha_contratacion:
            prof.fecha_contratacion = fecha_contratacion
        try:
            prof.salario = Decimal(request.POST.get('salario', str(prof.salario)))
        except:
            pass
        prof.save()

        # actualizar asignación de clases:
        seleccionadas = set(int(x) for x in request.POST.getlist('clases'))
        # quitar profesor de las clases que ya no están seleccionadas y que antes pertenecían al profesor
        for c in Clase.objects.filter(profesor=prof):
            if c.pk not in seleccionadas:
                c.profesor = None
                c.save()
        # asignar profesor a clases seleccionadas
        for cid in seleccionadas:
            try:
                c = Clase.objects.get(pk=cid)
                if c.profesor != prof:
                    c.profesor = prof
                    c.save()
            except Clase.DoesNotExist:
                continue

        return redirect('ver_profesor')
    return redirect('actualizar_profesor', pk=prof.pk)


def borrar_profesor(request, pk):
    prof = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        # antes de borrar, liberar las clases que tenía (opcional)
        Clase.objects.filter(profesor=prof).update(profesor=None)
        prof.delete()
        return redirect('ver_profesor')
    return render(request, 'profesor/borrar_profesor.html', {'profesor': prof})


# -------------------------
# MATERIAL - CRUD
# -------------------------

def ver_material(request):
    materiales = Material.objects.select_related('clase').all().order_by('nombre')
    return render(request, 'material/ver_material.html', {'materiales': materiales})

def agregar_material(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        tipo = request.POST['tipo']
        cantidad = request.POST['cantidad']
        proveedor = request.POST['proveedor']
        costo_unitario = request.POST['costo_unitario']
        fecha_compra = request.POST['fecha_compra']
        clase_id = request.POST['clase']

        clase = Clase.objects.get(id=clase_id)
        Material.objects.create(
            nombre=nombre,
            tipo=tipo,
            cantidad=cantidad,
            proveedor=proveedor,
            costo_unitario=costo_unitario,
            fecha_compra=fecha_compra,
            clase=clase
        )
        return redirect('ver_material')

    clases = Clase.objects.all()
    return render(request, 'material/agregar_material.html', {'clases': clases})

def actualizar_material(request, pk):
    mat = get_object_or_404(Material, pk=pk)
    clases = Clase.objects.all().order_by('nombre')
    return render(request, 'material/actualizar_material.html', {'material': mat, 'clases': clases})


def realizar_actualizacion_material(request, pk):
    mat = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        mat.nombre = request.POST.get('nombre', mat.nombre)
        mat.tipo = request.POST.get('tipo', mat.tipo)
        try:
            mat.cantidad = int(request.POST.get('cantidad', mat.cantidad))
        except:
            pass
        mat.proveedor = request.POST.get('proveedor', mat.proveedor)
        try:
            mat.costo_unitario = Decimal(request.POST.get('costo_unitario', str(mat.costo_unitario)))
        except:
            pass
        fecha_compra = request.POST.get('fecha_compra', None)
        if fecha_compra:
            mat.fecha_compra = fecha_compra
        clase_id = request.POST.get('clase', None)
        if clase_id:
            try:
                mat.clase = Clase.objects.get(pk=int(clase_id))
            except Clase.DoesNotExist:
                mat.clase = None
        else:
            mat.clase = None
        mat.save()
        return redirect('ver_material')
    return redirect('actualizar_material', pk=mat.pk)


def borrar_material(request, pk):
    mat = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        mat.delete()
        return redirect('ver_material')
    return render(request, 'material/borrar_material.html', {'material': mat})

