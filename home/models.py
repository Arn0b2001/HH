from django.db import models

# Create your models here.
class Signup(models.Model):
    email = models.CharField(max_length=50)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    
