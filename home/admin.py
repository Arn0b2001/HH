from django.contrib import admin
from home.models import Signup
from home.models import PropertyDetails
from home.models import Booking

# Register your models here.
admin.site.register(PropertyDetails)
admin.site.register(Signup)
admin.site.register(Booking)

