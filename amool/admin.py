from django.contrib import admin
from .models import Car, MercedesCar

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')  
    search_fields = ('name',)
    list_filter = ('price',)

admin.site.register(Car, CarAdmin)


class MercedesCarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model_year', 'price')
    search_fields = ('name',)
    list_filter = ('model_year', 'price')

admin.site.register(MercedesCar, MercedesCarAdmin)
