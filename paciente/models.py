from django.db import models
from clinica.models import Clinica
from ubigeo.models import Ubigeo

# Create your models here.

class Paciente(models.Model):
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, related_name='pacientes')
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField()
    ubigeo = models.ForeignKey(Ubigeo, on_delete=models.SET_NULL, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
    def save(self, *args, **kwargs):
        # Validar que el ubigeo pertenezca a la misma clínica
        if self.ubigeo and self.ubigeo.clinica != self.clinica:
            raise ValueError("El ubigeo debe pertenecer a la misma clínica del paciente")
        super().save(*args, **kwargs)
        
    
