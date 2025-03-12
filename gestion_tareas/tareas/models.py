from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre




class Tarea(models.Model):
    E_PENDING = "pendiente"
    E_INPROGRESS = "en progreso"
    E_COMPLETED = "completada"
    CHOICES_ESTADO = [
        (E_PENDING, "Pendiente"),
        (E_INPROGRESS, "En progreso"),
        (E_COMPLETED, "Completada"),    
    ]
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.CharField(choices=CHOICES_ESTADO, default=E_PENDING, max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo
