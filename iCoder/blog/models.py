from django.db import models

# Create your models here.
class Blog(models.Model):
    blogId=models.AutoField(primary_key=True)
    title=models.CharField( max_length=450)
    author=models.CharField( max_length=100)
    content=models.TextField()
    slug=models.CharField(max_length=100)
    Timestamp=models.DateTimeField()
    thumbnail=models.ImageField(upload_to ='blogs/uploads')
    
    def __str__(self):
        return self.title