from django.contrib import admin
from .models import  Tarea, Familia
# Register your models here.

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    pass

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    pass