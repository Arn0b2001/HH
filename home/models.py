from django.db import models

# Create your models here.
class Signup(models.Model):
    email = models.CharField(max_length=50)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    role = models.CharField(max_length=20, default = 'customer')

"""class Property(models.Model):
    owner = models.CharField(max_length=50)
    image_path = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

class OwnerModel(models.Model):
    owner_email = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)"""

class PropertyDetails(models.Model):
    ownwer_email = models.CharField(null = True, max_length=50)
    country = models.CharField(null = True, max_length=50)
    city = models.CharField(null = True, max_length=50)
    det_loc = models.CharField(null = True, max_length=50)
    price = models.CharField(null = True, max_length=50)
    types = models.CharField(null = True, max_length=50)
    bed = models.CharField(null = True, max_length=50)
    common_space = models.CharField(null = True, max_length=50)
    air_condition = models.BooleanField(null = True)
    parking = models.BooleanField(null = True)
    wifi = models.BooleanField(null = True)
    breakfast = models.BooleanField(null = True)
    verified = models.BooleanField(default = False)
    p_image = models.ImageField(null= True, upload_to='images/')
    view = models.CharField(null = True, max_length=50)
    

    
