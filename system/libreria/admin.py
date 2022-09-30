from django.contrib import admin
from .models import explanetas, userandpassword
#se crea superusuario para el django user: carlos y pass: solracn10
admin.site.register(explanetas)
admin.site.register(userandpassword)

