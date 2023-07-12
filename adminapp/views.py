from django.shortcuts import redirect, render
from django.contrib import messages
from accounts .models import Accounts
from productapp .models import Category,Product
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

def category(request):
    if 'admin_id' in request.session:
        item = Category.objects.all()
        return render(request,'admin/catogary.html',{'data': item })

def addcategory(request):
    if 'admin_id' in request.session:
        if request.method =='POST':
                category_name = str(request.POST['c_name'])
                category_name = category_name.upper()
                description   = request.POST['desc']
                if Category.objects.filter(category_name = category_name):
                    messages.error(request,"category alredy exists",extra_tags='categoryerror')
                    return redirect(addcategory)
                elif category_name == "" or description =="":
                    messages.error(request,"enter values")
                else:
                    item = Category.objects.create(
                        category_name = category_name,
                        description = description
                    )
                    return redirect(category)
                    
    return render(request,'admin/addcategory.html')

def delete_category(request,id):
    item = Category.objects.filter(id = id )
    item.delete()
    return redirect(category)

def edit_category(request,id):
    if 'admin_id' in request.session:
        item = Category.objects.get(id = id)
        if request.method =="POST":
            if Category.objects.filter(category_name = request.POST['c_name']) and request.POST['c_name'] != item.category_name:
                messages.error(request,'category already exists',extra_tags='')
                return render(request, 'admin/editcategory.html', {'data':item})
            elif request.POST['c_name'] == '' or request.POST['desc'] == '':
                messages.error(request,'enter the details',extra_tags='')
                return render(request, 'admin/editcategory.html', {'data':item})
            else:
                item.category_name   = request.POST['c_name'].upper()
                item.description     = request.POST['desc']
                item.save()
                return redirect(category)
        else:
            return render(request, 'admin/editcategory.html', {'data':item})

def coupen(request):
    return render(request,'admin/coupen.html')


def offer(request):
    return render(request,'admin/offer.html')

def order(request):
    return render(request,'admin/order.html')

def products(request):
    if 'admin_id' in request.session:
        item = Product.objects.filter(product_status = True).order_by("id")
        return render(request,'admin/products.html',{'data':item})
    else:
        messages.error(request, 'Only admin can access')
        return redirect(admin_login)

def add_product(request):
    if 'admin_id' in request.session:
        value = Category.objects.all()
        context = {
            'value' : value
        }
        if request.method == "POST":
            product_name = request.POST['p_name']
            description = request.POST['desc']
            price = request.POST['price']
            stock = request.POST['stock']
            category_name = request.POST['category']
            brand = request.POST['brand']
            image = request.FILES['uploadFromPC']
            image1 = request.FILES['uploadFromPC1']
            image2 = request.FILES['uploadFromPC2']

                
            if product_name == '' or description =='' or price=='' or stock==''or category_name == '' or brand==''or image=='' or image1=='' or image2 == '':
                messages.error(request,'All fields are required')
                return redirect(add_product)
            elif int(price)<0 or int(stock)<0:
                messages.error(request,'Negative number is not supportted for price and stock')
                return redirect(add_product)
            elif category_name == 'Select One':
                messages.error(request,'Please select a category')
                return redirect(add_product)
            if image == None:
                return redirect(add_product)
            product_status = request.POST['product_status']
            item = Product.objects.create(
                product_name=product_name,
                description=description,
                price=price,
                stock=stock,
                brand=brand,
                image=image,
                image1=image1,
                image2=image2,
                product_status=product_status
            )
        
            item.category = Category.objects.get(category_name = category_name)
            item.save()
            return redirect(products)
        return render(request,'admin/addproduct.html',context)
    else:
        messages.error(request, 'Only admin can access')
        return redirect(admin_login) 
    

    
def edit_product(request,id):
    if 'admin_id' in request.session:
        item = Product.objects.get(id = id)
        value =Category.objects.all()
        if request.method == 'POST':
            product_name = request.POST['p_name']
            description = request.POST['desc']
            price = request.POST['price']
            stock = request.POST['stock']
            category_name = request.POST['category']
            brand = request.POST['brand']
            try:
                image = request.FILES['uploadFromPC']
                image1 = request.FILES['uploadFromPC1']
                image2 = request.FILES['uploadFromPC2']
            except:
                print('please add an image!!')
            if product_name == '' or description =='' or price=='' or stock==''or category_name == '' or brand=='':
                messages.error(request,'All fields are required')
                return redirect('admin/edit_product')
            elif int(price)<0 or int(stock)<0:
                messages.error(request,'Negative number is not supportted for price and stock', extra_tags='productadderror')
                return redirect('admin/edit_product')
            item.product_name = request.POST['p_name']
            item.description = request.POST['desc']
            item.price = request.POST['price']
            item.stock = request.POST['stock']
            c_name = Category.objects.get(category_name = request.POST['category'])
            item.category = c_name
            item.brand = request.POST['brand']
            item.product_status = request.POST['product_status']
            try:       
                item.image = request.FILES['uploadFromPC']
                item.image1 = request.FILES['uploadFromPC1']
                item.image2 = request.FILES['uploadFromPC2']
            except:
                print('sdsdffdfdf')
                
            item.save()
            return redirect(products)
        return render(request, 'admin/product_edit.html',{'data':item, 'value':value})
    else:
        messages.error(request, 'Only admin can access')
        return redirect(admin_login)

            
        
def delete_product(request,id):
    if 'admin_id' in request.session:
        item = Product.objects.filter(id = id)
        item.delete()
        return redirect(products)
    
    
def sales(request):
    return render(request,'admin/sales.html')

def user_management(request):
    if 'admin_id' in request.session:
        item  =Accounts.objects.filter(is_admin = False).order_by('-id')
        return render(request,'admin/user_management.html',{'data':item})
def blockuser(request,id):
    item = Accounts.objects.get(id = id)
    if item.is_active  :
        item.is_active = False
    else:
        item.is_active = True
    item.save()
    return redirect(user_management)