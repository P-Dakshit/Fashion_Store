"""
URL configuration for my_first_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from emp import views

urlpatterns = [
    path('home/', views.home , name='home'),
    path('admin/', admin.site.urls , name='admin'),
    path('signup/', views.signup , name='signup'),
    path('', views.login_or_signup, name='login'),
    path('aboutus/', views.aboutus , name='aboutus'),
    path('cart/', views.cart , name='cart'),
    path('ecart/', views.ecart , name='ecart'),

    path('account/', views.account , name='account'),
    path('women/', views.women , name='women'),
    path('men/', views.men , name='men'),
    path('feedback/', views.feedback , name='feedback'),

    path('create-checkout-session/', views.create_checkout_session, name='checkout'),
    path('success.html/', views.success,name='success'),
    path('cancel.html/', views.cancel,name='cancel'),

]
