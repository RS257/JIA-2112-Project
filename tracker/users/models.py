from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


#Models for database. 
class Certificate(models.Model):
    certificate_name = models.CharField('Name', blank=True, max_length=250, default='', unique=True)
    is_published = models.BooleanField('Published', default=False)
    exp_interval = models.IntegerField('Expiration interval in days', blank = True, null = True)

    def __str__(self):
        return self.certificate_name

class Role(models.Model):
    role_name = models.CharField('Role', null=True, blank=True, max_length=250, default='', unique=True)
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
    # cert_duedate_list = {}

    def __str__(self):
        return self.profile_name.first_name + " " + self.profile_name.last_name

    def roles(self):
        return ", ".join([str(p) for p in self.roles_list.all()])

    def fullName(self):
        return self.profile_name.first_name + " " + self.profile_name.last_name

    # def certDuedateList(self):
    #     for i in self.roles_list.all(): 
    #         # for j in i.certificates_list.all():
    #         # if self.cert_duedate_list.get(i) in self.roles_list.all() :
    #         self.cert_duedate_list[i] = i #j.exp_interval
    #     return  self.cert_duedate_list

class Images(models.Model):
    certificate = models.ForeignKey(Certificate, default=None, null=False, blank=False, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, default=None, null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to = 'certificates/%Y/%m/%d/', null=True, blank=False)
    certification_completion_date = models.DateTimeField('Completion date', default=None, blank=False, null=True)
 
    def __str__(self):
        return self.certificate.certificate_name

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
        
                   



