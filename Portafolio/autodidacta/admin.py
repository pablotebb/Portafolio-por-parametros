from django.contrib import admin
from .models import Autodidacta


# Register your models here.
class AutodidactaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")  # Evita edición manual de campos automáticos


admin.site.register(Autodidacta, AutodidactaAdmin)
