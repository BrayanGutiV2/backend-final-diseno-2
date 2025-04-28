from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # o from django.contrib.auth.models import User si no usas modelo personalizado

# Si usas modelo personalizado
admin.site.register(CustomUser, UserAdmin)

# Si usas el modelo User por defecto
# admin.site.register(User, UserAdmin)