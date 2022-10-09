from django.contrib import admin
from .models import Profile, Role, RoleAssignment


class StateAdmin(admin.ModelAdmin):
    list_display = ('employee', 'occupation', )

admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(RoleAssignment, StateAdmin)