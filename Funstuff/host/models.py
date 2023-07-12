from django.db import models

# Create your models here.
class AddArt(models.Model):
    title = models.CharField("Title",max_length=300)
    desp = models.CharField("Description",max_length=300)
    image = models.ImageField(null=True,blank=True)
    # Date = models.DateField()