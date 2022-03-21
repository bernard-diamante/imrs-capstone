from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_ROLE_CHOICES = [
        (0, "Admin"),
        (1, "Main Office"),
        (2, "Warehouse Manager"),
        (3, "Site Manager")
    ]
    username = models.CharField(primary_key=True, max_length=3) # USE FOR USER LOGIN
    userFirstName = AbstractUser.first_name
    userMiddleName = models.CharField(max_length=50, blank=True)
    userLastName = AbstractUser.last_name
    userSuffix = models.CharField(max_length=30, blank=True)
    userEmail = AbstractUser.email
    userContactNo = models.CharField(max_length=11) 
    userRole = models.PositiveSmallIntegerField(default=3, choices=USER_ROLE_CHOICES)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = False
    def __str__(self):
        return self.username