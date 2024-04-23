from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('login', views.handlelogin, name = 'login'),
    path('logout', views.handlelogout, name = 'logout'),
    path('signup', views.signup, name = 'signup'),
    path('loggedin', views.loggedin, name = 'loggedin'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('editted', views.editted, name='editted'),
    path('property_det/<str:property_id>/', views.property_det, name='property_det'),
    path('property_add', views.property_add, name='property_add'),
    path('property_info', views.property_info, name='property_info'),
    path('verify_property/<str:property_id>/', views.verify_property, name='verify_property'),
    path('negotiation', views.negotiation, name = 'negotiation'),
    path('acceptoffer/<str:book_id>/', views.acceptoffer, name='acceptoffer'),
    path('rejectoffer/<str:book_id>/', views.rejectoffer, name='rejectoffer'),
    path('checkout/<str:book_id>/', views.checkout, name = 'checkout'),
    path('awaiting_enlistings', views.awaiting_enlistings, name = 'awaiting_enlistings'),
    path('awaiting_enlistings_det/<str:property_id>/', views.awaiting_enlistings_det, name = 'awaiting_enlistings_det'),
    path('overall_info', views.overall_info, name = 'overall_info'),
    path('complaints', views.complaints, name = 'complaints'),
    path('complaints_det/<str:complaint_id>/', views.complaints_det, name = 'complaints_det'),
    path('blacklist', views.blacklist, name = 'blacklist'),
    path('voucher', views.voucher, name = 'voucher'),
    path('admin_dash', views.admin_dash, name = 'admin_dash'),
    path('rental/<str:property_id>/', views.rental, name='rental'),
    path('customer_complaint/<str:book_id>/', views.customer_complaint, name='customer_complaint'),
    path('check_complaint/<str:book_id>/', views.check_complaint, name='check_complaint'),
    path('owner_profile/<str:owner>/', views.owner_profile, name='owner_profile'),
]
