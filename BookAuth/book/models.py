from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default=datetime.date.today)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth']

    def __str__(self):
        return self.email


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

