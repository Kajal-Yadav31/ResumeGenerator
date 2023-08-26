from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length=11)
    summary = models.TextField(max_length=200)
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    university = models.TextField(max_length=100)
    previous_work = models.TextField(max_length=100)
    skills = models.TextField(max_length=100)

