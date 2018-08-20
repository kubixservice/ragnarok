from django.contrib import admin

from . import models


class AdminVerification(admin.ModelAdmin):
    list_display = ('user', 'expiration_date', 'created_date', 'is_available')


admin.site.register(models.UserVerification, AdminVerification)
