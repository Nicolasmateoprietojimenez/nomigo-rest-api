from django.db import models

# Create your models here.

class TipoVinculacion(models.Model):
    descp_tipo_vinculacion = models.CharField(max_length=50)

    def __str__(self):
        return self.descp_tipo_vinculacion
    
class TipoNivelRiesgo(models.Model):
    descp_tipo_nivel_riesgo = models.CharField(max_length=50)
    porc_desc = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descp_tipo_nivel_riesgo
    
class NivelRiesgo(models.Model):
    desc_nivel_riesgo = models.CharField(max_length=50)
    id_tipo_nivel_riesgo = models.ForeignKey('TipoNivelRiesgo', on_delete=models.CASCADE)

    def __str__(self):
        return self.desc_nivel_riesgo
    
class Empresa(models.Model):
    nit = models.CharField(max_length=20, unique=True)
    id_empleado = models.ForeignKey('empleado.Empleado', on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=100)
    correo = models.EmailField()
    estado_sistema = models.CharField(max_length=20)

    def __str__(self):
        return self.razon_social
    
class Cargo(models.Model):
    nit = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    descp_cargo = models.CharField(max_length=50)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    id_nivel_riesgo = models.ForeignKey(NivelRiesgo, on_delete=models.CASCADE)
    nit = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.descp_cargo
    
class Vinculacion(models.Model):
    nro_documento = models.CharField(max_length=20)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    fecha_vinculacion = models.DateField()
    id_tipo_vinculacion = models.ForeignKey(TipoVinculacion, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey('empleado.Empleado', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nro_documento} - {self.id_cargo}'