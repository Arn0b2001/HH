from django.db import models
import uuid

# Create your models here.
class Signup(models.Model):

    email = models.CharField(max_length=50)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    role = models.CharField(max_length=20, default = 'customer')
    owned_property = models.IntegerField(default = 0)

class PropertyDetails(models.Model):
    ownwer_email = models.CharField(max_length=50)
    p_id = models.CharField(max_length=50, primary_key = True)
    property_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    det_loc = models.CharField(max_length=50)
    property_name = models.CharField(max_length=50)
    guest_num = models.IntegerField(default = 0)
    price = models.IntegerField()
    types = models.CharField(max_length=50)
    view = models.CharField(max_length=50)
    bed = models.CharField(max_length=50)
    common_space = models.CharField(max_length=50)
    tv = models.BooleanField()
    smoking = models.BooleanField()
    air_condition = models.BooleanField()
    bathroom = models.BooleanField()
    water_heater = models.BooleanField()
    parking = models.BooleanField()
    wifi = models.BooleanField()
    breakfast = models.BooleanField()
    verified = models.BooleanField(default = False)
    p_image1 = models.ImageField(null= True, upload_to='images/')
    p_image2 = models.ImageField(null= True, upload_to='images/')
    p_image3 = models.ImageField(null= True, upload_to='images/')
    p_image4 = models.ImageField(null= True, upload_to='images/')
    document = models.BooleanField(default = False)
    doc1 = models.FileField(upload_to='documents/')
    doc2 = models.FileField(upload_to='documents/')
    doc3 = models.FileField(upload_to='documents/')
    video = models.FileField(upload_to='videos/')
    

class Booking(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    price = models.IntegerField()
    neg_price = models.IntegerField(default = 0)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default = 'hold')
    payment_id = models.CharField(max_length=50, blank = True)
    

    
