"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = "HomeSpace Admin Portal"
admin.site.site_header = "HomeSpace Admin"
admin.site.index_title = "Welcome to HomeSpace Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forgot_password/', include('django.contrib.auth.urls')),
    path('forgot_password/password_reset', auth_views.PasswordResetView.as_view(
        subject_template_name='registration/password_reset_subject.txt')),
    path('', include('home.urls'))      
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
