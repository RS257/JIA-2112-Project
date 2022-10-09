from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Role(models.Model):
    name = models.CharField('Role', blank=True, max_length=50, default='')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    role = models.ManyToManyField(Role, through='RoleAssignment')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def getRole(self):
        return self.role

class RoleAssignment(models.Model):
    employee = models.ForeignKey(Profile, on_delete=models.CASCADE)
    occupation = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.user.first_name + " " + self.employee.user.last_name

    #prevent an employee from assigning for the same occupation twice 
    class Meta:
        unique_together = [['employee', 'occupation']]



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


