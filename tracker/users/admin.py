from django.contrib import admin
from .models import Profile, Role, Certificate
from django.db.models.functions import Concat


class StateAdminProfile(admin.ModelAdmin):
    list_display = ('profile_name', 'fullName', 'roles')

class StateAdminRole(admin.ModelAdmin):
    list_display = ('role_name', 'certificates')

admin.site.register(Profile, StateAdminProfile)
admin.site.register(Role, StateAdminRole)
admin.site.register(Certificate)
