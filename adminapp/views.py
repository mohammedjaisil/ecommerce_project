from django.shortcuts import redirect, render
from django.contrib import messages
from accounts .models import Accounts
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request,'admin/admin_index.html')


def admin_login(request):
    if "admin_id" in request.session:
        return redirect(index)
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if password=="" and username=="":
            messages.error(request,"please enter the values!!")
        elif Accounts.objects.filter(username = username):
            admin=authenticate(username=username,password=password)
            if admin is not None:
                request.session['admin_id']=username
                login(request,admin)
                return redirect(index)
            else:
                messages.error(request,"admin not found")
                return redirect(admin_login)
        else:
            messages.error(request,"admin not found")
            return redirect (admin_login)
   
    return render(request,'admin/admin_login.html')


def admin_logout(request):
    if "admin_id" in request.session:
        del request.session["admin_id"]
        logout(request)
        return redirect(admin_login)
    return render(request,'admin/login.html')

def catogary(request):
    return render(request,'admin/catogary.html')

def addcatogary(request):
    return render(request,'admin/addcategory.html')

def coupen(request):
    return render(request,'admin/coupen.html')


def offer(request):
    return render(request,'admin/offer.html')

def order(request):
    return render(request,'admin/order.html')

def products(request):
    return render(request,'admin/products.html')

def add_product(request):
    return render(request,'admin/addproduct.html')

def sales(request):
    return render(request,'admin/sales.html')

def user_management(request):
    if 'admin_id' in request.session:
        item  =Accounts.objects.all().order_by('-id')
        return render(request,'admin/user_management.html',{'data':item})
def blockuser(request,id):
    item = Accounts.objects.get(id = id)
    if item.is_active  :
        item.is_active = False
    else:
        item.is_active = True
    item.save()
    return redirect(user_management)