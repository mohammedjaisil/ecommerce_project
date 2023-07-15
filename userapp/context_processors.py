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
        category = Category.objects.all()
        cart_count =0
        if order_qs.exists():
            orders = order_qs[0]
            cart_count = orders.items.count()
        return {
            'cart_count': cart_count,
            'category':category
        }
    elif request.session.session_key:
        user = request.session.session_key
        order_qs = Order.objects.filter(items__guest_user = user,orderd = False)
        category = Category.objects.all()
        cart_count =0
        if order_qs.exists():
            orders = order_qs[0]
            cart_count = orders.items.count()
        return {
         
            'cart_count': cart_count,
            'category':category
        }
    else:
        
        category = Category.objects.all()
        return {
         
            'cart_count': 0,
            'category':category
        }
        
