from django.urls import path,include
from .import views
urlpatterns = [
    path('admin_dashboard',views.index,name='admin_dashboard'),
    path('',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('category',views.category,name='category'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('editcategory/<int:id>',views.edit_category,name='editcategory'),
    path('deletecategory/<int:id>',views.delete_category,name='deletecategory'),
    path('edit_product/<int:id>',views.product_edit,name='edit_product'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('coupen',views.coupen,name='coupen'),
    path('offer',views.offer,name='offer'),
    path('order',views.order,name='order'),
    path('products',views.products,name='products'),
    path('sales',views.sales,name='sales'),
    path('user_management',views.user_management,name='user_management'),
    path('add_product',views.add_product,name='add_product'),
    path('blockuser/<int:id>',views.blockuser,name='blockuser'),
    

]