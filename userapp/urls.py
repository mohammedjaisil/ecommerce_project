from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('categoryfilter/<str:value>',views.selectedView,name='categoryfilter'),
    path('login',views.login,name='login'),
    path('sign_up',views.signup,name='signup'),
    path('cart',views.cart,name='cart'),
    path('cartadd',views.cartadd,name='cartadd'),
    path('otp_login',views.otp_login,name='otp_login'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout'),
    path('add_address',views.add_address,name='add_address'),
    path('deleteaddress/<int:id>',views.delete_address,name='deleteaddress'),
    path('edit_address/<int:id>',views.edit_address,name='edit_address'),
    path('profile_edit',views.profile_edit,name='profile_edit'),
    path('product_deatils/<int:id>',views.product_deatils,name='product_deatils'),
    path('deleteFromCart/<int:id>',views.deleteFromCart,name='deleteFromCart'),
    path('checkout',views.checkout,name='checkout'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('wishlistadd/<int:id>',views.wishlistadd,name='wishlistadd'),
    path('wishlistdelete/<int:id>',views.wishlistdelete,name='wishlistdelete'),
    path('payment',views.payment,name='payment'),
    path('sortwithprice/<str:value>/<str:category>',views.sortwithprice,name='sortwithprice'),



]
