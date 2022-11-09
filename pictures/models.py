from django.db import models

# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField

class Picture(models.Model):
  image = CloudinaryField('image')