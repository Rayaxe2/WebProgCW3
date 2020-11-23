from django.db import models

# Create your models here.
class SiteUser(models.Model):
    Username = models.CharField(max_length=30, primary_key=True)
    Password = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    DOB = models.DateField()

    def __str__(self):
        return self.Username
