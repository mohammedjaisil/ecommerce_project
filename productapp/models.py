from django.db import models
from accounts.models import Accounts

# Create your models here.



class Catogary(models.Model):
    catogary_name  = models.CharField(max_length=100)
    description    = models.TextField(max_length=200)
    catogary_offer = models.IntegerField(null=True,default=0,blank=True)
    
    def __str__(self):
        return self.catogary_name
    
    class meta:
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories'
        
        
class Product(models.Model):
    product_name   = models.CharField(max_length=100)
    description    = models.TextField(max_length=2000,null=True)
    price          = models.IntegerField(null=True)
    stock          = models.IntegerField(null=True)
    Catogary       = models.ForeignKey(Catogary,on_delete=models.CASCADE,null=True,blank=True)
    brand          = models.CharField(max_length=200,null=True,blank=True)
    product_offer  = models.IntegerField(default=0,null=True,blank=True)
    image          = models.ImageField(null=True,blank=True,upload_to='image/')
    image1         = models.ImageField(null=True,blank=True,upload_to='image/')
    image2         = models.ImageField(null=True,blank=True,upload_to='image/')
    product_status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.product_name
    
    class meta:
        verbose_name        = 'product'
        verbose_name_plural = 'products'
    