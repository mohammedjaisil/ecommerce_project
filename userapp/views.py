from django.shortcuts import redirect, render
from django.contrib import messages
from accounts .models import Accounts
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request,'user/user_index.html')


def login(request):
    if 'user_id'in request.session:
        return redirect(index)
    elif request.method== 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        if username =='' or password =='':
            messages.error(request,"please enter the values!")
            return redirect(login)
        elif Accounts.objects.filter(username = username):
            data=Accounts.objects.get(username = username)
            if data.is_active == False :
                messages.error(request,'your account got blocked')
                return redirect(login)
            user= authenticate(username = username ,password =password)
            if user is not None :
                request.session['user_id']=username
                return redirect (index)
            else:
               messages.error(request, 'Invalid Credentials!!!')
               return redirect(login)
        else:
               messages.error(request, 'user not exist!!!')
               return redirect(login)
    return render(request,'user/login.html')

def signup(request):
    if request.method=='POST':
        first_name   = request.POST['first_name']
        username     = request.POST['username']
        email        = request.POST['email']
        phone_number = request.POST['phone_number']
        password     = request.POST['pass']
        password1    = request.POST['pass1']
        
        if password==password1 or len(password)>6:
            try:
                k=int(request.POST['phone_number'])
            except:
                messages.error(request,"please enter a phone number")
                return redirect(signup)
            if first_name == '' or username == '' or email == '' or phone_number =='' or password == '':
                messages.error(request,"name must not be empty")
                messages.error(request,"username must not be empty")
                messages.error(request,"email must not be empty")
                messages.error(request,"phone number must not be empty")
                messages.error(request,"password must not be empty")
                return redirect (signup)
            elif len(phone_number)!=10:
                messages.error(request,"please enter a valid number")
                return redirect(signup)
            elif Accounts.object.filter(username=username):
                messages.error(request,"username already exists")
                return redirect(signup)
            elif Accounts.object.filter(phone=phone_number):
                messages.error(request,"phone number already exists")
                return redirect(signup)
            elif Accounts.object.filter(email=email):
                messages.error(request,"email already exists")
                return redirect(signup)
            else:
                item=Accounts.object.create(
                    first_name=first_name,
                    username=username,
                    email=email,
                    phone=phone_number,
                    password=password
                )
                request.session['user_id']=username
                item.save()
        else:
            messages.error(request,"password must be same and more then 6 charecters")
            return redirect(signup)
        
        
    return render(request,'user/sign_up.html')

def cart(request):
    return render(request,'user/cart.html')

def cartempty(request):
    return render(request,'user/cartempty.html')

def otp_login(request):
    return render(request,'user/otp_login.html')