from django.contrib import admin
from .models import Personal


# Register your models here.
class PersonalAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")  # Evita edición manual de campos automáticos


admin.site.register(Personal, PersonalAdmin)