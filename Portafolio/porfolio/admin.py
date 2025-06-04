from django.contrib import admin
from .models import Card, Carrousel


# Register your models here.
class CardAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")  # Evita edición manual de campos automáticos

# Register your models here.
class CarrouselAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")  # Evita edición manual de campos automáticos



admin.site.register(Card, CardAdmin)
admin.site.register(Carrousel, CarrouselAdmin)