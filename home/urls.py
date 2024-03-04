from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('login', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('loggedin', views.loggedin, name = 'loggedin'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('editted', views.editted, name='editted'),
    path('property_det', views.property_det, name='property_det'),
    path('property_add', views.property_add, name='property_add'),
]