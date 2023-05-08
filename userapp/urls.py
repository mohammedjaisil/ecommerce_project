from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login,name='login'),
    path('sign_up',views.signup,name='signup'),
    path('cart',views.cart,name='cart'),
    path('cartempty',views.cartempty,name='cartempty'),
    path('otp_login',views.otp_login,name='otp_login'),
]
