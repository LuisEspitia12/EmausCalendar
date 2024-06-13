from django.contrib import admin

# Register your models here.
from .models import Pais, Parroquia, Grupo, Ciudad, Coordinador

admin.site.register(Parroquia)
admin.site.register(Pais)
admin.site.register(Grupo)
admin.site.register(Coordinador)
admin.site.register(Ciudad)