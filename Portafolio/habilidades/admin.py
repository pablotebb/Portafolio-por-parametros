from django.contrib import admin
from .models import Habilidad


# Register your models here.
class HabilidadAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")  # Evita edición manual de campos automáticos


admin.site.register(Habilidad, HabilidadAdmin)