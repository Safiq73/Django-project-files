from unicodedata import category
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default='General')
    heading0=models.CharField(max_length=500, default='' )
    content_heading0=models.CharField(max_length=5000, default='' )
    heading1=models.CharField(max_length=500, default='' )
    content_heading1=models.CharField(max_length=5000, default='' )
    heading2=models.CharField(max_length=500, default='' )
    content_heading2=models.CharField(max_length=5000, default='' )
    publish_date=models.DateField(default="")
    thumbnail=models.ImageField(upload_to="shop/images", default="")
    
    def __str__(self):
        return self.title