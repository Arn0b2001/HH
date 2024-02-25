from django.shortcuts import render, redirect
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

        signup_data = User.objects.create_user(first_name= f_name, last_name = l_name, email = email, 
                                        username = email, password = password)
        signup_data.save()
        return redirect('/login')
        
    return render(request, 'signup.html')

def loggedin(request):
    """if request.user.is_anonymous:
        return redirect('/login')"""
    return render(request, 'loggedin.html')
