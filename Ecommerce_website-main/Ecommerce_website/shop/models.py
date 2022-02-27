from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50 )
    desc=models.CharField(max_length=200)
    publish_date=models.DateField(default="")
    product_image=models.ImageField(upload_to="shop/images", default="")
    category= models.CharField(max_length=50, default="")
    subcategory= models.CharField(max_length=50, default="")
    price=models.IntegerField(default="0")
    
    def __str__(self):
        return self.product_name
    
    
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50 )
    email=models.CharField(max_length=50 )
    phone=models.CharField(max_length=50 )
    desc=models.CharField(max_length=400)
    
    def __str__(self):
        return self.name
    
    
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000, default='My json')
    name=models.CharField(max_length=50 )
    amount=models.IntegerField(default=0)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=5000)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=200, default="")
    
    def __str__(self):
        return self.name
    
    
class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default=1)
    update_desc=models.CharField(max_length=5000)
    timeStamp=models.DateField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.update_desc[0, 10] +'...'