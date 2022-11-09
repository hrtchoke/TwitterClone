from operator import truediv
from django.db import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cloudinary.models import CloudinaryField

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=200)
  
    def __str__(self):
        return f"{self.task}"
class Post(models.Model):
    class Meta(object):
        db_table = 'post'
        ordering = ['-created_at',]
    
    name = models.CharField(
        'Name', blank=False,null=False,max_length = 14,db_index=True,default='Anonymous'
    )
    body = models.CharField(
                'Body', blank=True,null=False,max_length = 140,db_index=True

    )
    image = CloudinaryField(
        'image', blank=True,null=True,db_index=True
    )
    likecount = models.IntegerField(
        'Like',default=0,null=True,blank=True
    )
    created_at = models.DateTimeField (
        'Created DateTime', blank=True, auto_now_add=True

    )