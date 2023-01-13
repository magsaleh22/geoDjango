from django.contrib import admin
from .models import *

# Register your models here.
class MunicipalitiesAdmin(admin.ModelAdmin):
    list_display = (['name'])
    
    
admin.site.register(Municipalities,MunicipalitiesAdmin)
admin.site.register(User)
