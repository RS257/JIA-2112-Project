from django.contrib import admin
from .models import Profile, Role, Certificate, Images
from django.db.models.functions import Concat

class StateImageAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'profile', 'certification_completion_date')

class ImagesAdmin(admin.StackedInline):
    model = Images

class StateAdminProfile(admin.ModelAdmin):
    list_display = ('profile_name', 'fullName', 'roles')
    inlines = [ImagesAdmin]

    class Meta:
       model = Profile

class StateAdminRole(admin.ModelAdmin):
    list_display = ('role_name', 'certificates')

def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)
make_published.short_description = "Publish"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)
make_unpublished.short_description = "Unpublish"

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_name', 'exp_interval', 'is_published')
    actions = [make_published, make_unpublished]

#Register models to show them in admin portal
admin.site.register(Profile, StateAdminProfile)
admin.site.register(Role, StateAdminRole)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Images, StateImageAdmin)

admin.site.site_header = 'Valient School District'

