from django.contrib import admin

# Register your models here.
from .models import Post
from .models import *

  
admin.site.register(Todo)
admin.site.register(Post)
