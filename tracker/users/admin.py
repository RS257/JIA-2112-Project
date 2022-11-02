from django.contrib import admin
from .models import Profile, Role, Certificate, Images
from django.db.models.functions import Concat

class StateImageAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'profile', 'certification_completion_date', 'certification_due_date', 'is_valid')

class ImagesAdmin(admin.StackedInline):
    model = Images

def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
make_active.short_description = "Make active"

def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)
make_inactive.short_description = "Make inactive"    

class StateAdminProfile(admin.ModelAdmin):
    list_display = ('profile_name', 'fullName', 'roles', 'is_active')
    exclude = ('counter',)
    inlines = [ImagesAdmin]
    actions = [make_active, make_inactive]

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

admin.site.site_header = 'Valliant Certification Tracker'

