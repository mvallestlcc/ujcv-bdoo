from django.db import models

# Create your models here.

class Puestos(models.Model):
    puestoId = models.BigIntegerField(primary_key=True)
    puestoNombre = models.CharField(max_length=70)

    def __str__(self):
        return str(self.puestoId) + ' ' + self.puestoNombre

class Departamentos(models.Model):
    DeptoId = models.IntegerField(primary_key=True)
    DeptoNombre = models.CharField(max_length=100)

    def __str__(self):
    	return str(self.DeptoId) + ' ' + self.DeptoNombre
    
    

class TipoEmpleado(models.Model):
    TipoEmpId = models.IntegerField(primary_key=True)
    TipoEmpNombre = models.CharField(max_length=50)
    
    def __str__(self):
    	return str(self.TipoEmpId) + ' ' + self. TipoEmpNombre

class Expediente(models.Model):
    identidad = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    correo = models.EmailField()
    puestoId = models.ForeignKey(Puestos,null=False, blank=False, default=0, on_delete=models.PROTECT)
    DepartamentoId = models.ForeignKey(Departamentos, null=False, blank=False, default=0, on_delete=models.PROTECT )
    TipoEmpleado = models.ForeignKey(TipoEmpleado, null=True, blank=True, default=0, on_delete=models.PROTECT)

    def __str__(self):
        return self.identidad + ' ' + self.nombre + ' ' + self.apellido





    

