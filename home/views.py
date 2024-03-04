import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.conf import settings
from home.models import Signup
from home.models import PropertyDetails
# Create your views here.

def index(request):
    """if request.user.is_anonymous:
        return redirect('/login')"""
    return render(request, 'index.html')

def login(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username = email, password = password)
        if user is not None:
            request.session['email'] = user.username
            auth.login(request,user)
            return redirect('/loggedin')
   return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        f_name = request.POST.get('firstname')
        l_name = request.POST.get('lastname')
        country  = request.POST.get('country')
        country_code = request.POST.get('countrycode')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        signup_alldata = Signup( email = email, f_name = f_name, l_name = l_name, country = country, 
                             country_code = country_code, mobile = mobile)
        signup_alldata.save()

        signup_data = User.objects.create_user(email = email, username = email, password = password)
        signup_data.save()
        return redirect('/login')
        
    return render(request, 'signup.html')

def loggedin(request):
    """if request.user.is_anonymous:
        return redirect('/login')"""
    properties = PropertyDetails.objects.all()
    return render(request, 'loggedin.html',{'properties': properties})

def get_user_data(request):
    email_check = request.session.get('email')
    if email_check:
        user_data = get_object_or_404(Signup, email=email_check)
        return user_data
    

def profile(request):
    user_data = get_user_data(request)
    print(user_data.email)
    return render(request, 'profile.html', {'user_data': user_data})

def edit_profile(request):
    user_data = get_user_data(request)
    return render(request, 'edit_profile.html', {'user_data': user_data})


def editted(request): 
    if request.method == 'POST':
        user_data = get_user_data(request)
        if user_data:
            user_data.f_name = request.POST.get('f_name')
            user_data.l_name = request.POST.get('l_name')
            user_data.country  = request.POST.get('country')
            user_data.country_code = request.POST.get('countrycode')
            user_data.mobile = request.POST.get('mobile')
            user_data.save()  # Save the changes to the database
            return redirect('/profile')
        

def property_det(request):
    return render(request, 'property_det.html')

def property_add(request):
    if request.method == 'POST':
        user_data = get_user_data(request)
        user_data.role = 'owner'
        user_data.save()
        ownwer_email = user_data.email
        country = request.POST.get('country')
        city = request.POST.get('city')
        det_loc = request.POST.get('det_loc')
        price = request.POST.get('price')
        types = request.POST.get('types')
        bed = request.POST.get('bed')
        common_space = request.POST.get('common_space')
        air_condition = request.POST.get('aircondition')
        parking = request.POST.get('parking')
        wifi = request.POST.get('wifi')
        view = request.POST.get('view')
        breakfast = request.POST.get('breakfast')
        p_image = request.FILES.getlist('p_image[]')
        property_alldata = PropertyDetails(country = country, city = city, det_loc = det_loc, 
                             price = price, types = types, bed = bed, common_space = common_space, air_condition = air_condition,
                             parking = parking, wifi = wifi, breakfast = breakfast, ownwer_email = ownwer_email, view = view)
        property_alldata.save()
        for i in range(len(p_image)):
            image = p_image[i]
            image.name = f'{ownwer_email[:-4]}property{i}.png'
            property_alldata.p_image = image
            property_alldata.save()
        return redirect('/property_add')
        
    return render(request, 'property_add.html')




