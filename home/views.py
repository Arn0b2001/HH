from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from home.models import Signup
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
    return render(request, 'loggedin.html')

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
