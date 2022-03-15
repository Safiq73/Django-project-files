from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
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
    
class BlogComment(models.Model):
    sNo=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    # Here on_delete means if you delete the parent record this record will be automatically deleted
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent=models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    # here self is to make the foreign key from the same table
    timeStamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[:max(len(self.comment), 15)]+'...'