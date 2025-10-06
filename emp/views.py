from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse 
from .models import cloth,product
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from django.conf import settings
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_or_signup(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            try:
                user = User.objects.get(username=email)
                messages.error(request, "Incorrect password. Please try again.")
            except User.DoesNotExist:
                messages.error(request, "User does not exist. Please sign up.")
            return render(request, "login.html", {'error_message': "Invalid username or password. Please try again."})
    return render(request, "login.html")
        
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email  
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            cloth.objects.create(user=user, email=email, username=username)
            login(request, user)
            return redirect('home')
        except IntegrityError:
            return render(request, "signup.html", {'error_message': "User with this email already exists."})
    return render(request, "signup.html")

@login_required
def home(request):
    if request.method == 'POST':
        # Assuming the form contains product details such as image link, product name, and price
        image_link = request.POST.get('image_link')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        # user=request.user
        # Create a CartItem object and save it to the database


        product.objects.create(image_link=image_link, product_name=product_name, product_price=product_price, user=request.user)

        # Redirect the user back to the home page or wherever you want
        return redirect('home')
    else:
        # Render the home page with any necessary context data
        return render(request, 'home.html')
    # return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")

@login_required
def account(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'account.html', context)
    # return render(request,"account.html")

def cart(request):
    if request.method == 'GET' :
        product_name = request.GET.get('product_name')
        product_price = request.GET.get('product_price')
        image_link = request.GET.get('image_link')
        if product_name and product_price and image_link:
            return render(request, 'cart.html', {'product_name': product_name, 'product_price': product_price, 'image_link': image_link})
        else:
            return render(request, 'cart.html')  # Render an empty cart message
    else:
        return HttpResponseNotAllowed(['GET'])
    
def ecart(request):
    return render(request,"ecart.html")
    
def women(request):
    return render(request,"women.html")

def men(request):
    return render(request,"men.html")


def success(request):
    return render(request, 'success.html')

def feedback(request):
    return render(request,"feedback.html")

def cancel(request):
    return render(request, 'home.html')

stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'

@csrf_exempt
def create_checkout_session(request):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'INR',
                    'product_data': {
                        'name': 'Grand Total',
                    },
                    'unit_amount':319900,  # Amount in cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return JsonResponse({'sessionId': session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=403)
