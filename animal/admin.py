from django.contrib import admin

# Register your models
from .models import *

admin.site.register(Zoo)
admin.site.register(Animal)
admin.site.register(Especie)