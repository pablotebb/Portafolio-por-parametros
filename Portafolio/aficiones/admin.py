from django.contrib import admin
from .models import Hobby


# Register your models here.
class HobbyAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")  # Evita edición manual de campos automáticos


admin.site.register(Hobby, HobbyAdmin)