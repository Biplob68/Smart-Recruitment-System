from django.db import models

# Create your models here.


class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=111, default="")
    phone = models.CharField(max_length=12, default="")
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
