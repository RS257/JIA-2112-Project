from django.contrib import admin
from .models import Profile, Role, Certificate, Images
from django.db.models.functions import Concat

class ImagesAdmin(admin.StackedInline):
    model = Images

class StateAdminProfile(admin.ModelAdmin):
    list_display = ('profile_name', 'fullName', 'roles')
    inlines = [ImagesAdmin]

    class Meta:
       model = Profile

class StateAdminRole(admin.ModelAdmin):
    list_display = ('role_name', 'certificates')

#Register models to show them in admin portal
admin.site.register(Profile, StateAdminProfile)
admin.site.register(Role, StateAdminRole)
admin.site.register(Certificate)
admin.site.register(Images)
