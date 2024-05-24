from django.contrib import admin
from .models import Package, Plans,Continents

# Register your models here.

admin.site.register(Continents) 
admin.site.register(Package) 
admin.site.register(Plans)