from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

def validate_capitalized(value):
    if value != value.capitalize():
        raise ValidationError('Invalid (not capitalized) value: %(value)s',
                              code='invalid',
                              params={'value': value})

class User(AbstractUser):
    USER_ROLE_CHOICES = [
        (0, "Admin"),
        (1, "Main Office"),
        (2, "Warehouse Manager"),
        (3, "Site Manager")
    ]
    username = models.CharField(primary_key=True, max_length=3, validators=[MinLengthValidator(3)]) # USE FOR USER LOGIN
    first_name = models.CharField(max_length=20, blank=True)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    suffix = models.CharField(max_length=30, blank=True)
    contact_number = models.CharField(max_length=11) 
    role = models.PositiveSmallIntegerField(default=3, choices=USER_ROLE_CHOICES)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = False
    def __str__(self):
        return self.username

