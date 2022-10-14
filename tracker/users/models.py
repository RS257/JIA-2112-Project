from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


#Models for database. 
class Certificate(models.Model):
    certificate_name = models.CharField('Name', blank=True, max_length=150, default='')

    def __str__(self):
        return self.certificate_name

class Role(models.Model):
    role_name = models.CharField('Role', null=True, blank=True, max_length=150, default='')
    certificates_list = models.ManyToManyField(Certificate, blank=True)
        
    def __str__(self):
        return self.role_name

    def certificates(self):
        return ", ".join([str(p) for p in self.certificates_list.all()])    

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

class Profile(models.Model):
    profile_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    roles_list = models.ManyToManyField(Role, blank=True)

    def __str__(self):
        return self.profile_name.first_name + " " + self.profile_name.last_name

    def roles(self):
        return ", ".join([str(p) for p in self.roles_list.all()])

    def fullName(self):
        return self.profile_name.first_name + " " + self.profile_name.last_name

class Images(models.Model):
    profile = models.ForeignKey(Profile, default=None, null=True, blank=True, on_delete=models.CASCADE)
    image_name = models.CharField('Certificate name', null=True, blank=False, max_length=50, default='')
    images = models.FileField(upload_to = 'certificates/%Y/%m/%d/', null=True, blank=True)
 
    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"           



