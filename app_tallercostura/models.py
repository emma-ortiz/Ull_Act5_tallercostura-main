from django.db import models

# ==========================================
# MODELO: ALUMNO
# ==========================================
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: PROFESOR
# ==========================================
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: CLASE
# ==========================================
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion_horas = models.IntegerField()
    nivel = models.CharField(max_length=50, choices=[
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ])
    cupo_maximo = models.IntegerField()

    # 🔗 Relaciones
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='clases', null=True, blank=True)
    alumnos = models.ManyToManyField('Alumno', through='Inscripcion', related_name='clases')

    def __str__(self):
        return f"{self.nombre} ({self.nivel})"


# ==========================================
# MODELO: INSCRIPCION
# ==========================================
class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50, choices=[
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
    ])
    monto_pagado = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.alumno} → {self.clase}"


# ==========================================
# MODELO: MATERIAL
# ==========================================
class Material(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    proveedor = models.CharField(max_length=100)
    costo_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_compra = models.DateField()

    # ✅ Cada material pertenece a UNA clase
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='materiales')

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"
