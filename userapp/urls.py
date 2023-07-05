from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login,name='login'),
    path('sign_up',views.signup,name='signup'),
    path('cart',views.cart,name='cart'),
    path('cartempty',views.cartempty,name='cartempty'),
    path('otp_login',views.otp_login,name='otp_login'),
    path('profile/',views.profile,name='profile'),
    path('logout',views.logout,name='logout'),
    path('add_address',views.add_address,name='add_address'),
    path('deleteaddress/<int:id>/',views.delete_address,name='deleteaddress'),
    path('edit_address/<int:id>',views.edit_address,name='edit_address'),
    path('profile_edit',views.profile_edit,name='profile_edit'),
    path('category_dd',views.selectedviews,name='category_dd'),
]
