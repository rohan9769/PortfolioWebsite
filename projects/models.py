from django.db import models

# Create your models here.
class Projects(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    #url = models.URLField(max_length=1000000)



