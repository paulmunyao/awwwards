from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    description = models.TextField(max_length=100)
    link = models.URLField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()
    overall = models.IntegerField()
   
