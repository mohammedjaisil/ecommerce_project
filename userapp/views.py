from django.shortcuts import redirect, render
from django.contrib import messages
from accounts .models import Accounts,CustomerAdress
from productapp .models import Category,Product,CartItem,Order,MyWishList
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    if not request.session.session_key:
        request.session.save()
    if 'user_id' in request.session:
        item        = Product.objects.all().order_by("id")
        category    = Category.objects.all()
        user        = Accounts.object.get(username = request.session['user_id'])
        wish        = MyWishList.objects.filter(username = user.id)
        wishlist    = []
        for i in wish:
            wishlist.append(i.product.product_name)
        context  = {
            'data':item,
            'category':category,
            'wishlist':wishlist
        }
    else:
        item        = Product.objects.all().order_by("id")
        wishlist  = []
        context     = {
                'data':item,
                'wishlist':wishlist
            }
        
    
    return render(request,'user/index.html',context)



def selectedView(request,value):
    category = Category.objects.get(category_name = value)
    selected = category.category_name
    item     = Product.objects.filter(category = category.id).order_by("id")
    category = Category.objects.all()
    wishlist = []
    if 'user_id' in request.session:
        user      = Accounts.object.get(username = request.session['user_id'])
        wish      = MyWishList.objects.filter(username = user.id)
        for i in wish:
            wishlist.append(i.product.product_name)
        print(wishlist)
    context  = {
        'data':item,
        'category':category,
        'selected':selected,
        'wishlist':wishlist
    }
    return render(request, 'user/index.html',context)


def profile(request):
    if 'user_id' in request.session:
        user    = request.session['user_id']
        user_id = Accounts.objects.get(username = user)
        address = CustomerAdress.objects.filter(user = user_id)
        
        context = {
            'address' : address
        }
        
    else:
        context = None
    return render(request,'user/profile.html',context)



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
            user = authenticate(username = username ,password = password)
            if user is not None:
                request.session['user_id']=username
                return redirect(index)
            else:
               messages.error(request, 'Invalid Credentials!!!')
               return redirect(login)
        else:
               messages.error(request, 'user not exist!!!')
               return redirect(login)
    return render(request,'user/login.html')


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        return redirect(index)
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
            elif Accounts.objects.filter(username=username):
                messages.error(request,"username already exists")
                return redirect(signup)
            elif Accounts.objects.filter(phone=phone_number):
                messages.error(request,"phone number already exists")
                return redirect(signup)
            elif Accounts.objects.filter(email=email):
                messages.error(request,"email already exists")
                return redirect(signup)
            else:
                item=Accounts.objects.create(
                    first_name=first_name,
                    username=username,
                    email=email,
                    phone=phone_number,
                    
                )
                item.set_password(password)
                item.save()
                request.session['user_id']=username
                return redirect(index)
            
        else:
            messages.error(request,"password must be same and more then 6 charecters")
            return redirect(signup)
        
        
    return render(request,'user/sign_up.html')


def add_address(request):
    if 'user_id' in request.session:
        if request.method == "POST":
            user         = request.session.get('user_id')
            first_name   = request.POST['first_name']
            last_name    = request.POST['last_name']
            email        = request.POST['email']
            phone_number = request.POST['phone_number']
            house_name   = request.POST['house_name']
            state        = "Kerala"
            country      = "India"
            street_name  = request.POST['street_name']
            city         = request.POST['city']
            post_code    = request.POST['post_code']
            
            item = CustomerAdress.objects.create(
                first_name   = first_name,
                last_name    = last_name,
                email        = email,
                phone_number = phone_number,
                house_name   = house_name,
                state        = state,
                country      = country,
                street_name  = street_name,
                city         = city,
                post_code    = post_code
            )
            
            item.user = Accounts.objects.get(username =user)   
            item.save()
            return redirect(profile)   
        
    else :
        if request.method == "POST":
            user         = request.session.session_key
            order_qs     = Accounts.objects.filter(guest_user = user)
            first_name   = request.POST.get('first_name')
            last_name    = request.POST.get('last_name')
            email        = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            house_name   = request.POST.get('house_name')
            state        = "Kerala"
            country      = "India"
            street_name  = request.POST.get('street_name')
            city         = request.POST.get('city')
            post_code    = request.POST.get('post_code')
            if order_qs.exists():
                item = CustomerAdress.objects.create(
                    first_name   = first_name,
                    last_name    = last_name,
                    email        = email,
                    phone_number = phone_number,
                    house_name   = house_name,
                    state        = state,
                    country      = country,
                    street_name  = street_name,
                    city         = city,
                    post_code    = post_code,
                    guest_user   = user
                )
                item.save()
                return redirect(checkout) 
            else:
                order_qs = Accounts.objects.create(guest_user = user)
                item = CustomerAdress.objects.create(
                    first_name   = first_name,
                    last_name    = last_name,
                    email        = email,
                    phone_number = phone_number,
                    house_name   = house_name,
                    state        = state,
                    country      = country,
                    street_name  = street_name,
                    city         = city,
                    post_code    = post_code,
                
                )
                item.user = Accounts.objects.get(guest_user = user)  
                item.save()
                return redirect(checkout) 
    return render(request,'user/addaddress.html')

def edit_address(request,id):
    item = CustomerAdress.objects.get(id = id)
    if request.method == "POST":
        item.first_name   = request.POST["first_name"]
        item.last_name    = request.POST['last_name']
        item.email        = request.POST['email']
        item.phone_number = request.POST['phone_number']
        item.house_name   = request.POST['house_name']
        item.state        = 'kerala'
        item.country      = 'india'
        item.street_name  = request.POST['street_name']
        item.city         = request.POST['city']
        item.post_code    = request.POST['post_code']
        
        item.save()
        return redirect(profile)
    context = {
        'item' : item
    }
        
    return render(request, 'user/editaddress.html',context)


def delete_address(request,id):
        item = CustomerAdress.objects.get(id = id)
        item.delete()
        return redirect(profile)

    
    
def cart(request):
    if 'user_id' in request.session:
        user     = request.session.get('user_id')
        order_qs = Order.objects.filter(user__username = user, orderd=False).order_by('date_ordered')
        cart_qs  = CartItem.objects.filter(user__username = user)
        if order_qs.exists() and cart_qs.exists():
            order_object = order_qs[0]
        else:
            return render(request,'user/cartempty.html')
        context = {
            'order_object' : order_object
        }
    else:
        user     = request.session.session_key
        order_qs = Order.objects.filter(guest_user = user, orderd=False).order_by('date_ordered')
        cart_qs  = CartItem.objects.filter(guest_user = user)
        if order_qs.exists() and cart_qs.exists():
            order_object = order_qs[0]
        else:
            return render(request,'user/cartempty.html')
        context = {
            'order_object' : order_object
        }
    return render(request,'user/cart.html', context)

def checkout(request):
    if 'user_id' in request.session:
        user    = request.session['user_id']
        user_id = Accounts.objects.get(username = user)
        address = CustomerAdress.objects.filter(user = user_id)
        order_qs = Order.objects.filter(user__username = user, orderd=False).order_by('date_ordered')
        cart_qs  = CartItem.objects.filter(user__username = user)
        if order_qs.exists() and cart_qs.exists():
            order_object = order_qs[0]
        else:
            return render(request,'user/cartempty.html')
        if order_qs.exists():
            order = order_qs[0]
        else:
            order= Order.objects.create(user_id=user_id.id)
        if order_qs.exists():
            orders       = order_qs[0]
            total_amount = float(orders.total_amount_cart)
            tax          = (total_amount) * 3 /100

            
                
            grand_total = float(total_amount) + float(tax)
            grand_total = "{:.1f}".format(grand_total)
            grand_total = float(grand_total)
        else:
            messages.error(request, 'Please add an product',extra_tags='ordererror')
            return render(request,'user/cartempty.html')
        context = {
            'address' : address,
            'order_object' : order_object,
            'order' : order,
            'cart':cart_qs,
            'grand_total' :grand_total,
        }
        
    else:
        user     = request.session.session_key
        address = CustomerAdress.objects.filter(guest_user = user)
        order_qs = Order.objects.filter(guest_user = user, orderd=False).order_by('date_ordered')
        cart_qs  = CartItem.objects.filter(guest_user = user)
        if order_qs.exists() and cart_qs.exists():
            order_object = order_qs[0]
        else:
            return render(request,'user/cartempty.html')
        if order_qs.exists():
            order = order_qs[0]
        else:
            order= Order.objects.create(user_id=user_id.id)
        if order_qs.exists():
            orders       = order_qs[0]
            total_amount = float(orders.total_amount_cart)
            tax          = (total_amount) * 3 /100

            
                
            grand_total = float(total_amount) + float(tax)
            grand_total = "{:.1f}".format(grand_total)
            grand_total = float(grand_total)
        else:
            messages.error(request, 'Please add an product',extra_tags='ordererror')
            return render(request,'user/cartempty.html')
        context = {
            'order_object' : order_object,
            'order' : order,                
            'address' : address,
            'cart':cart_qs,
            'grand_total' :grand_total,        }
    return render(request,'user/checkout.html',context)


def cartadd(request):
    if 'user_id' in request.session:
        product_id   = request.POST.get('product-id')
        quantity     = int(request.POST.get('product-quantity'))
        product_var  = Product.objects.get(id = product_id)
        user         = request.session.get('user_id')
        item         = Accounts.objects.get(username =user)
        id           = item.id
        Order_qs     = Order.objects.filter(user_id = id ,orderd = False)
        if Order_qs.exists():
            order = Order_qs[0]
            if order.items.filter(user_id = id ,product = product_var).exists():
                order_item         =order.items.get(user_id = id, product =product_var)
                order_item.quantity += quantity
                order_item.save()
                return redirect('/product_deatils/'+str(product_id))
            else:
                order_item = CartItem.objects.create(user_id=id, product = product_var, quantity=quantity)
                order.items.add(order_item)
                order.save()
                return redirect('/product_deatils/'+str(product_id))
            
        else:
            order      = Order.objects.create(user_id=id)
            order_item = CartItem.objects.create(user_id=id, product=product_var, quantity=quantity)
            order.items.add(order_item)
            order.save()
            return redirect('/product_deatils/'+str(product_id))
    else:
        product_id   = request.POST.get('product-id')
        quantity     = int(request.POST.get('product-quantity'))
        product_var  = Product.objects.get(id = product_id)
        id           = request.session.session_key
        order_qs     = Order.objects.filter(guest_user= id, orderd = False)
        if order_qs.exists():
            order = order_qs[0]
            if order.items.filter( guest_user=id, product=product_var).exists():
                order_item           = order.items.get( guest_user=id, product=product_var)
                order_item.quantity += quantity
                order_item.save()
                return redirect('/product_deatils/'+str(product_id))
            else:
                order_item = CartItem.objects.create(guest_user=id, product = product_var, quantity=quantity)
                order.items.add(order_item)
                order.save()       
                return redirect('/product_deatils/'+str(product_id))
        else:
            order      = Order.objects.create(guest_user=id)
            order_item = CartItem.objects.create(guest_user=id, product=product_var, quantity=quantity)
            order.items.add(order_item)
            order.save()
            return redirect('/product_deatils/'+str(product_id))

        

def deleteFromCart(request,id):
    item = CartItem.objects.get( id = id)
    item.delete()
    return redirect(cart)

def otp_login(request):
    # item = Accounts.objects.filter(first_name='abcd')
    # for i in item:
    #     print(i.first_name)
    return render(request,'user/otp_login.html')

def profile_edit(request):
        if 'user_id' in request.session:
            user = request.session['user_id']
            item = Accounts.objects.get(username=user)
        
            if request.method =='POST':
                first_name   = request.POST['first_name']
                email        = request.POST['email']
                phone_number = request.POST['phone_number']
                try:
                    k=int(request.POST['phone_number'])
                except:
                    messages.error(request,"please enter a phone number")
                    return redirect(profile_edit)
                if first_name == ''  or email == '' or phone_number =='':
                    messages.error(request,"name must not be empty")
                    messages.error(request,"email must not be empty")
                    messages.error(request,"phone number must not be empty")
                    return redirect (profile_edit)
                elif len(phone_number)!=10:
                    messages.error(request,"please enter a valid number")
                    return redirect(profile_edit)          
                elif Accounts.objects.filter(phone=phone_number) :
                    messages.error(request,"phone number already exists")
                    return redirect(profile_edit)
                elif Accounts.objects.filter(email=email):
                    messages.error(request,"email already exists")
                    return redirect(profile_edit)
                else:
                    item.first_name    = first_name
                    item.phone         = phone_number
                    item.email         = email
                    item.save()
                    return redirect(profile)
                
                
            else:
                return render(request,'user/profile_edit.html', {'data' : item})
            
def product_deatils(request,id):
    
    item = Product.objects.get(id = id)
    
    return render(request,'user/products.html', {'thisProduct' : item})
def wishlist(request):
    if 'user_id' in request.session:
        user = Accounts.objects.get(username = request.session.get('user_id'))
        item = MyWishList.objects.filter(username = user.id)
        
        context = {
            'data':item
        }
        return render(request,'user/whishlist.html',context)
    else:
        messages.error(request,'login requiered')
        return redirect(login)
    
    
    
    

def wishlistadd(request, id):
    if 'user_id' in request.session:
        user     = request.session.get('user_id')
        user     = Accounts.object.get(username = user)
        product  = Product.objects.get(id = id)
        if MyWishList.objects.filter(username_id = user.id,product_id = product.id):
            return redirect(index)
        if MyWishList.objects.filter(id=product.id).exists():
            return redirect(index)
        else:
            item = MyWishList.objects.create(username_id = user.id,product_id = product.id )
            item.save()
            return redirect(index)
    else:
        messages.error(request, 'Login is required')
        return redirect(login)



def wishlistdelete(request,id):
    if 'user_id' in request.session:
        user     = request.session.get('user_id')
        user     = Accounts.object.get(username = user)
        item     = MyWishList.objects.get(username = user.id , product = id)
        item.delete()
        return redirect(index)

    else:
        messages.error(request, 'Login is required')
        return redirect(login)



def payment(request):
    
    return render(request,'user/payment.html')