from django.contrib import admin
from .models import explanetas, userandpassword
#se crea superusuario para el django user: carlos y pass: carlos
admin.site.register(explanetas)
admin.site.register(userandpassword)

