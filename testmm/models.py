from django.db import models


# Create your models here.
class ImgTest(models.Model):
    img_url = models.ImageField(upload_to='img')
