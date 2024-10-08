from django.db import models
from django.contrib.auth.models import User


class basep1(models.Model):
    class Meta:
        __tablename__ = 'basep1'

    field1 = models.CharField(max_length=250)
    Marcatemporal = models.CharField(max_length=250)
    MATRICULA = models.CharField(max_length=250)
    NOMBRECOMPLETO = models.CharField(max_length=250)
    FOTODELTRABAJADOR = models.CharField(max_length=250)
    FOTODELAFIRMA = models.CharField(max_length=250)
    FECHADENACIMIENTO = models.CharField(max_length=250)
    CATEGORIA = models.CharField(max_length=250)
    CENTRODETRABAJOACTUAL = models.CharField(max_length=250)
    ADSCRIPCIONESANTERIORES = models.CharField(max_length=250)
    TURNO = models.CharField(max_length=250)
    DOMICILIOPARTICULAR = models.CharField(max_length=250)
    COLONIA = models.CharField(max_length=250)
    MUNICIPIO = models.CharField(max_length=250)
    SECCIONAL= models.CharField(max_length=250)
    NUMERODECELULAR= models.CharField(max_length=250)
    CORREO= models.CharField(max_length=250)
    ENCARGADODEESTRUCTURA= models.CharField(max_length=250)
    RESPONSABLEDE100= models.CharField(max_length=250)
    RESPONSABLEDE10= models.CharField(max_length=250)
    PARTICIPACIONESDELTRABAJADOR = models.CharField(max_length=250)
    INFORMACIONADICIONAL= models.CharField(max_length=250)
    DESCANSOS= models.CharField(max_length=250)  
    VACACIONESPROGRAMADAS= models.CharField(max_length=250)
    SERVICIO= models.CharField(max_length=250)
    PROMOCION= models.CharField(max_length=250)
    MOVILIZACION= models.CharField(max_length=250)
    MIRESPONSABLE= models.CharField(max_length=250)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
