from django.contrib import admin
from home.models import Signup
from home.models import PropertyDetails
from home.models import Booking
from home.models import Review
from home.models import Complaint
from home.models import Blacklist


# Register your models here.
admin.site.register(PropertyDetails)
admin.site.register(Signup)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Complaint)
admin.site.register(Blacklist)

