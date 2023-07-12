from django.db import models
import django.utils.timezone as timezone
from django.core.validators import MinValueValidator, MaxValueValidator,MinLengthValidator, MaxLengthValidator
import uuid


# Create your models here.


class Data(models.Model):
    name_file = models.CharField(max_length=10)
    name_group = models.CharField(max_length=15, primary_key = True)
    file = models.FileField()

class Feedback(models.Model):
    name_proff = models.CharField(max_length=20)
    lesson = models.CharField(max_length=40, primary_key = True)
    name_group = models.CharField(max_length=15)
    comment = models.TextField()

class User(models.Model):
    name_user = models.CharField(max_length=55)
    name_group = models.CharField(max_length=25, primary_key = True)
    mail = models.EmailField()
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8)])
    name_specialization = models.CharField(max_length=10)
    name_university = models.CharField(max_length=35)
    year = models.IntegerField(default=timezone.now().year, validators=[MinValueValidator(timezone.now().year-6), MaxValueValidator(timezone.now().year+1)])
    in_group=models.BooleanField(default=True)
    moder=models.BooleanField(default=False)
    
    class Meta:
        verbose_name='Человек'
        verbose_name_plural='Человеки'


