from django.urls import path,include
from .import views
urlpatterns = [
    path('admin_dashboard',views.index,name='admin_dashboard'),
    path('',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('catogary',views.catogary,name='catogary'),
    path('coupen',views.coupen,name='coupen'),
    path('offer',views.offer,name='offer'),
    path('order',views.order,name='order'),
    path('products',views.products,name='products'),
    path('sales',views.sales,name='sales'),
    path('user_management',views.user_management,name='user_management'),
    path('add_product',views.add_product,name='add_product'),

]