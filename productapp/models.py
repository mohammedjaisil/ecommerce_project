from django.db import models
from accounts.models import Accounts,CustomerAdress
import uuid
# Create your models here.



class Category(models.Model):
    category_name  = models.CharField(max_length=100)
    description    = models.TextField(max_length=200)
    category_offer = models.IntegerField(null=True,default=0,blank=True)
    
    def __str__(self):
        return self.category_name
    
    class meta:
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories'
        
        
class Product(models.Model):
    product_name   = models.CharField(max_length=100)
    description    = models.TextField(max_length=2000,null=True)
    price          = models.IntegerField(null=True)
    stock          = models.IntegerField(null=True)
    category       = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    brand          = models.CharField(max_length=200,null=True,blank=True)
    product_offer  = models.IntegerField(default=0,null=True,blank=True)
    image          = models.ImageField(null=True,blank=True,upload_to='image/')
    image1         = models.ImageField(null=True,blank=True,upload_to='image/')
    image2         = models.ImageField(null=True,blank=True,upload_to='image/')
    product_status = models.BooleanField(default=True)
    
    
    
    
    class meta:
        verbose_name        = 'product'
        verbose_name_plural = 'products'
    
    
    

class CartItem(models.Model):
    user = models.ForeignKey(Accounts,on_delete= models.CASCADE, null= True ,blank = True) 
    product = models.ForeignKey(Product,on_delete= models.CASCADE, null= True ,blank = True)
    quantity = models.IntegerField(default=1,null = True ,blank= True)
    size = models.CharField(max_length=50,null = True ,blank= True)
    date_added = models.DateField(auto_now_add=True)
    guest_user  = models.CharField(max_length=200,null=True, blank=True)
    cancel_status = models.BooleanField(default=False, null=True, blank=True)
    reason          = models.CharField(max_length=255,null= True,blank = True)


    

    
STATUS_CHOICES = (
    ("Confirmed" , "Confirmed"),
    ("Shipped" , "Shipped"),
    ("Out for delivery" , "Out for delivery"),
    ("Delivered" , "Delivered"),
    ("Canceled" , "Canceled"),
    ("Returned", "Returned"),

)

class Order(models.Model):
    user            = models.ForeignKey(Accounts,on_delete= models.CASCADE, null = True ,blank = True )
    orderd          = models.BooleanField(default=False)
    Customer        = models.ForeignKey(CustomerAdress,on_delete= models.CASCADE, null = True ,blank = True )
    date_ordered    = models.DateField(auto_now_add= True)
    status          = models.CharField(choices=STATUS_CHOICES,max_length=100,default='Confirmed')
    items           = models.ManyToManyField(CartItem,blank = True )
    transaction_id  = models.UUIDField(default=uuid.uuid4, editable=False,null=True, blank = True)
    payment_method  = models.CharField(max_length=50,null= True,blank = True  )
    total_price     = models.FloatField(null = True ,blank= True)
    date_delivered  = models.DateField(auto_now_add= False,default='2022-01-01')
    guest_user      = models.CharField(max_length=200,null=True, blank=True)
    returnexpiry    = models.BooleanField(default=True,null=True, blank=True)
    reason          = models.CharField(max_length=255,null= True,blank = True)
    discount        = models.CharField(max_length=255,null= True,blank = True, default = "0")
   
   
   
class MyWishList(models.Model):
    username         = models.ForeignKey(Accounts,on_delete= models.CASCADE, null= True ,blank = True) 
    product     = models.ForeignKey(Product,on_delete= models.CASCADE, null= True ,blank = True)
    def __str__(self):
         return str(self.username)