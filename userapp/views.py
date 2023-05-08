from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'user/user_index.html')


def login(request):
    return render(request,'user/login.html')

def signup(request):
    return render(request,'user/sign_up.html')

def cart(request):
    return render(request,'user/cart.html')

def cartempty(request):
    return render(request,'user/cartempty.html')

def otp_login(request):
    return render(request,'user/otp_login.html')