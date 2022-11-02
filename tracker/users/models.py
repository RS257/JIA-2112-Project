from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils import timezone



class Certificate(models.Model):
    certificate_name = models.CharField('Name', blank=True, max_length=250, default='', unique=True)
    is_published = models.BooleanField('Published', default=False)
    exp_interval = models.IntegerField('Expiration interval in days', blank = True, null = True, default=0) 

    def __str__(self):
        return self.certificate_name

class Role(models.Model):
    role_name = models.CharField('Role', null=True, blank=True, max_length=250, default='', unique=True)
    certificates_list = models.ManyToManyField(Certificate, blank=True)
        
    def __str__(self):
        return self.role_name

    #Returns a list of certificate this role is assigned to
    def certificates(self):
        return ", ".join([str(p) for p in self.certificates_list.all()])    

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        

class Profile(models.Model):
    profile_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    roles_list = models.ManyToManyField(Role, blank=True)
    is_active = models.BooleanField('Active', default=True) #If user is active, the user will be rendered in the frontend
    counter =  models.IntegerField(default=0) #The variable is used in dashboard.html to calculate the number of valid certificates

    def __str__(self):
        return self.profile_name.first_name + " " + self.profile_name.last_name

    #Returns a list of roles the profile is assigned to
    def roles(self):
        return ", ".join([str(p) for p in self.roles_list.all()])

    #Returns the full name of a user
    def fullName(self):
        return self.profile_name.first_name + " " + self.profile_name.last_name

    #Return the number of certificates the profile is assigned to. The method is used in dashboard.html
    def getNumberOfCerts(self):
        i = 0
        for role in self.roles_list.all():
            for cert in role.certificates_list.all():
                i += 1
        return i 

    #Increments a counter in dashboard.html to find out the number of valis certificates for a profile
    def inrementCounter(self):
        self.counter += 1    

            

#Returns a path to upload an image 
def getPathToSave(instance, filename):
    return '/'.join(['certificates', str(instance.profile.profile_name.last_name) + " " + str(instance.profile.profile_name.first_name), str(datetime.now().year), str(datetime.now().month), str(datetime.now().day), instance.certificate.certificate_name, filename])

class Images(models.Model):
    certificate = models.ForeignKey(Certificate, default=None, null=False, blank=False, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, default=None, null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to = getPathToSave, null=True, blank=False)
    certification_completion_date = models.DateTimeField('Completion date', default=None, blank=False, null=True)
    certification_due_date = models.DateTimeField('Due date', default= None, blank=True, null=True)
    is_valid = models.BooleanField('Valid', default=True)

    def __str__(self):
        return self.certificate.certificate_name

    #Returns the due date for an uploaded image(certificate). This method is used in views.py
    def getDueDate(self):
        self.certification_due_date = self.certification_completion_date + timedelta(days= self.certificate.exp_interval)
        return self.certification_due_date

    #Truncates everything before an image name and return the name. This method is used in base_dashboard.html and dashboard.html
    def getName(self):
        return str(self.file).rsplit('/', 1)[-1]    

    #Returns a boolean value that indicates if a certificate is valid or not. The methos if used in base_dashboard.html and dashboard.html
    def isValid(self):
        return self.getDueDate() >= timezone.now()
        
    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
        
                   


