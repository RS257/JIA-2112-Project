from django.contrib import admin
from .models import Profile, Role, Certificate
#, RoleAssignment
from django.db.models.functions import Concat


# class StateAdmin(admin.ModelAdmin):
#     list_display = ('employee', 'occupation', )

class StateAdmin(admin.ModelAdmin):
    list_display = ('user', 'fullName', 'roles')

admin.site.register(Profile, StateAdmin)
admin.site.register(Role)
admin.site.register(Certificate)
# admin.site.register(RoleAssignment, StateAdmin)