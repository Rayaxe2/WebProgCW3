from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class SiteUser(User):
    #UserID = models.AutoField(primary_key=True)
    #username = models.CharField(max_length=150, primary_key=True)
    #Password = models.CharField(max_length=255)
    #Email = models.EmailField(max_length=255)
    DOB = models.DateField()

    def __str__(self):
        return self.username
