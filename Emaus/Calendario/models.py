from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}, {self.pais}"

class Parroquia(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Coordinador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Asume que usas el sistema de usuarios de Django
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Grupo(models.Model):
    nombre = models.CharField(max_length=255)
    numero_de_retiro = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    valor_retiro = models.DecimalField(max_digits=10, decimal_places=2)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    coordinador = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    telefono_inscripcion_whatsapp = models.CharField(max_length=20)
    formulario_inscripcion = models.URLField()
    correo_electronico = models.EmailField()
    casa_de_retiro = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='Emaus/Calendario/static/img/posters')

    def __str__(self):
        return self.nombre


