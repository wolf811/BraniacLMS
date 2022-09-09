from django.contrib import admin
from authapp import models
# Register your models here.


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "is_active", "date_joined"]
    ordering = ["-date_joined"]
