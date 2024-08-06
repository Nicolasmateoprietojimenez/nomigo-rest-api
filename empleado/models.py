from django.db import models

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    desc_rol = models.CharField(max_length=50)
    permisos = models.TextField()

    def __str__(self):
        return self.desc_rol
    
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nro_documento = models.CharField(max_length=20, unique=True)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    estado_sistema = models.BooleanField(default=True)
    telefono = models.CharField(max_length=20)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado_civil = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
