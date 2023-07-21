from accounts.models import *
from productapp.models import *


def checkid(request):
    if 'user_id' in request.session:
        logi = request.session.get('user_id')
        if Accounts.objects.filter(username = logi):
            user = Accounts.objects.get(username = logi)
        else:
            user = None
        return {
            'user' : user
        }
    else:
        return { 'user' : None}
        
def add_variable_to_context(request):
    if 'user_id' in request.session:
        user = request.session['user_id']
        order_qs = Order.objects.filter(user__username=user,orderd = False)
        wishlist_count = MyWishList.objects.filter(username__username=user).count()
        category = Category.objects.all()
        cart_count =0
        total_amount = 0
        if order_qs.exists():
            orders = order_qs[0]
            total_amount= float(orders.total_amount_cart)
            cart_count = orders.items.count()
        tax = (total_amount) * 3 /100

        return {
            'total_amount':total_amount,
            'tax': tax,
            'cart_count': cart_count,
            'category':category,
            'tax_amount':total_amount+tax,
            'wishlist_count':wishlist_count
        }
    elif request.session.session_key:
        user = request.session.session_key
        order_qs = Order.objects.filter(items__guest_user = user,orderd = False)
        wishlist_count = MyWishList.objects.filter(username__username=user).count()
        category = Category.objects.all()
        cart_count =0
        total_amount=0
        if order_qs.exists():
            orders = order_qs[0]
            total_amount= float(orders.total_amount_cart)
            cart_count = orders.items.count()
        tax = (total_amount) * 3 /100
        return {
            'total_amount':total_amount,
            'tax': tax,
            'cart_count': cart_count,
            'tax_amount':total_amount+tax,
            'category':category,
            'wishlist_count':wishlist_count
        }
    else:
        
        category = Category.objects.all()
        return {
         
            
            'total_amount':0,
            'tax_amount':0,
            'tax': 0,
            'cart_count': 0,
            'wishlist_count':0,
            'category':category
        }
        
