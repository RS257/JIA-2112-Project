from django.db import models

class Student(models.Model):
    firstName = models.CharField("First Name", max_length=240)
    lastName = models.CharField("Last Name", max_length=240)
    email = models.EmailField()
#     document = models.CharField("Document", max_length=20)
    password = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name