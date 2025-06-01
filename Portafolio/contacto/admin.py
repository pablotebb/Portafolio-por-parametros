from django.contrib import admin
from .models import Contacto


# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")  # Evita edición manual de campos automáticos


admin.site.register(Contacto, ContactoAdmin)