import os
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Func, Value as V
from django.db.models.functions import Lower, Replace
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from home.models import Signup
from home.models import PropertyDetails, Booking
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create your views here.

l1 = ['']
def index(request):
    if request.method == "POST":
        search = request.POST.get('search')
        types = request.POST.get('types')
        if search == None:
            search = l1[0]
        else:
            l1[0] = search

        place = search
        if len(search) == 0 and types == None:
            properties = PropertyDetails.objects.all()
        elif len(search) == 0 and types != None:
            properties = PropertyDetails.objects.filter(types__icontains=types)
            error = f'No {types} is enlisted'
        elif len(search) != 0 and types != None:
            search = search.replace(' ', '').lower()
            properties = PropertyDetails.objects.annotate(country_normalized=Func(Lower('country'), V(' '), V(''), 
            function='replace'), city_normalized=Func(Lower('city'), V(' '), V(''), function='replace'),).filter(
            Q(country_normalized__icontains=search) | Q(city_normalized__icontains=search), 
            types__icontains=types)
            if len(properties) != 0 and properties[0].city.lower().replace(' ','') == search:
                place = properties[0].city
                l1[0] = place
            elif len(properties) != 0:
                place = properties[0].country
                l1[0] = place
            error = f'{types}s can\'t be found in {place}'
            if len(properties) != 0:
                messages.success(request,f'{types}s in {place}')
        elif len(search) != 0 and types == None:
            search = search.lower().replace(' ', '')
            properties = PropertyDetails.objects.annotate(country_normalized=Func(Lower('country'), V(' '), V(''), 
            function='replace'), city_normalized=Func(Lower('city'), V(' '), V(''), function='replace'),).filter(
            Q(country_normalized__icontains=search) | Q(city_normalized__icontains=search))
            print(properties)
            if len(properties) != 0 and properties[0].city.lower().replace(' ','') == search:
                place = properties[0].city
                l1[0] = place
            elif len(properties) != 0:
                place = properties[0].country
                l1[0] = place
            
            error = f'{place} can\'t be found'

        if len(properties) == 0:
            messages.error(request,error)
            properties = PropertyDetails.objects.all()
    else:
        place = ''
        properties = PropertyDetails.objects.all()
    return render(request, 'index.html',{'properties': properties, 'place':place})

def handlelogin(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = email, password = password)
        if user is not None:
            login(request, user)
            request.session['email'] = user.username
            messages.success(request, 'Sucessfully logged in')
            return redirect('/loggedin')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')
   return render(request, 'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, 'Sucessfully logged out')
    return redirect('/')
        

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        f_name = request.POST.get('firstname')
        l_name = request.POST.get('lastname')
        country  = request.POST.get('country')
        country_code = request.POST.get('countrycode')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('/signup')
            
        else:
            signup_alldata = Signup( email = email, f_name = f_name, l_name = l_name, country = country, 
                             country_code = country_code, mobile = mobile)
            signup_alldata.save()
            signup_data = User.objects.create_user(email = email, username = email, password = password)
            signup_data.save()
            return redirect('/login')
        
    return render(request, 'signup.html')

l = ['']
def loggedin(request):
    if request.method == "POST":
        search = request.POST.get('search')
        types = request.POST.get('types')
        if search == None:
            search = l[0]
        else:
            l[0] = search

        place = search
        if len(search) == 0 and types == None:
            properties = PropertyDetails.objects.all()
        elif len(search) == 0 and types != None:
            properties = PropertyDetails.objects.filter(types__icontains=types)
            error = f'No {types} is enlisted'
        elif len(search) != 0 and types != None:
            search = search.replace(' ', '').lower()
            properties = PropertyDetails.objects.annotate(country_normalized=Func(Lower('country'), V(' '), V(''), 
            function='replace'), city_normalized=Func(Lower('city'), V(' '), V(''), function='replace'),).filter(
            Q(country_normalized__icontains=search) | Q(city_normalized__icontains=search), 
            types__icontains=types)
            if len(properties) != 0 and properties[0].city.lower().replace(' ','') == search:
                place = properties[0].city
                l[0] = place
            elif len(properties) != 0:
                place = properties[0].country
                l[0] = place
            error = f'{types}s can\'t be found in {place}'
            if len(properties) != 0:
                messages.success(request,f'{types}s in {place}')
        elif len(search) != 0 and types == None:
            search = search.lower().replace(' ', '')
            properties = PropertyDetails.objects.annotate(country_normalized=Func(Lower('country'), V(' '), V(''), 
            function='replace'), city_normalized=Func(Lower('city'), V(' '), V(''), function='replace'),).filter(
            Q(country_normalized__icontains=search) | Q(city_normalized__icontains=search))
            print(properties)
            if len(properties) != 0 and properties[0].city.lower().replace(' ','') == search:
                place = properties[0].city
                l[0] = place
            elif len(properties) != 0:
                place = properties[0].country
                l[0] = place
            
            error = f'{place} can\'t be found'

        if len(properties) == 0:
            messages.error(request,error)
            properties = PropertyDetails.objects.all()
        
    else:
        place = ''
        properties = PropertyDetails.objects.all()
    return render(request, 'loggedin.html',{'properties': properties, 'place' : place})

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
        

def property_det(request,property_id):
    property = get_object_or_404(PropertyDetails, p_id=property_id)
    booking = Booking.objects.all()
    if request.method == 'POST':
        neg_price = request.POST.get('neg_price')
        check_in = request.POST.get('check_in')
        check_in = datetime.strptime(check_in, '%d/%m/%Y').date()
        check_out = request.POST.get('check_out')
        check_out = datetime.strptime(check_out, '%d/%m/%Y').date()
        guests = request.POST.get('guests')
        customer = get_user_data(request).email
        booking_data = Booking(property = property_id, customer = customer, price = property.price, neg_price = neg_price, 
                               check_in = check_in, check_out = check_out, guests = guests)
        booking_data.save()

        return render(request, 'property_det.html',{'property': property, 'booking' : booking})
    
    return render(request, 'property_det.html',{'property': property, 'booking' : booking})

def property_add(request):
    if request.method == 'POST':
        user_data = get_user_data(request)
        user_data.role = 'owner'
        print(PropertyDetails.objects.filter(ownwer_email = user_data.email).count())
        user_data.owned_property += 1
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
        p_id = f'{ownwer_email[:-4]}property{user_data.owned_property}'
        property_name = request.POST.get('property_name')
        guest_num = request.POST.get('guest_num')
        bathroom = request.POST.get('bathroom')
        smoking = request.POST.get('smoking')
        water_heater = request.POST.get('water_heater')
        tv = request.POST.get('tv')
        property_alldata = PropertyDetails(p_id = p_id, country = country, city = city, det_loc = det_loc, 
                             price = price, types = types, bed = bed, common_space = common_space, air_condition = air_condition,
                             parking = parking, wifi = wifi, breakfast = breakfast, ownwer_email = ownwer_email, view = view,
                             property_name = property_name, guest_num = guest_num, bathroom = bathroom, smoking = smoking,
                             water_heater = water_heater, tv = tv)
        property_alldata.save()
        
        image = p_image[0]
        image.name = f'{property_alldata.p_id}image{1}.png'
        property_alldata.p_image1 = image

        image = p_image[1]
        image.name = f'{property_alldata.p_id}image{2}.png'
        property_alldata.p_image2 = image

        image = p_image[2]
        image.name = f'{property_alldata.p_id}image{3}.png'
        property_alldata.p_image3 = image

        image = p_image[3]
        image.name = f'{property_alldata.p_id}image{4}.png'
        property_alldata.p_image4 = image
        property_alldata.save()
        user_data.save()
        return redirect('/loggedin')
        
    return render(request, 'property_add.html')

def property_info(request):
     email = get_user_data(request).email
     properties = PropertyDetails.objects.filter(ownwer_email=email)
     return render(request, 'property_info.html', {'properties': properties})

def verify_property(request, property_id):
    property = get_object_or_404(PropertyDetails, p_id=property_id)
    if request.method == 'POST':
        property.doc1 = request.FILES.get('document1')
        property.doc2 = request.FILES.get('document2')
        property.doc3 = request.FILES.get('document3')
        property.video = request.FILES.get('video')
        property.document = True
        property.save()
        return redirect('/property_info')
    return render(request, 'verify_property.html', {'property': property})

def negotiation(request):
    bookings = Booking.objects.all()
    properties = PropertyDetails.objects.all()
    email = get_user_data(request).email
    offers = []
    c = 1
    for i in bookings:
        for j in properties:
            if j.ownwer_email == email and i.property == j.p_id:
                offer = {'booking': i, 'property': j, 'offer_number': c}
                offers.append(offer)
                c += 1
    return render(request, 'negotiation_notification.html', {'offers':offers})

def acceptoffer(request, book_id):
    accepted = get_object_or_404(Booking, book_id=book_id)
    accepted.status = 'accepted'
    accepted.save()
    bookings = Booking.objects.all()
    for booking in bookings:
        if accepted.book_id != booking.book_id and accepted.property == booking.property:
            booking.delete()#needs to change
    return redirect('/property_info')

def rejectoffer(request, book_id):
    rejected = get_object_or_404(Booking, book_id=book_id)
    rejected.status = 'rejected'
    rejected.save()
    return redirect('/property_info')

def customer_complaint(request):
    return render(request, 'customer_complaint.html')