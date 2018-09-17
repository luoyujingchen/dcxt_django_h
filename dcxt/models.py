from django.db import models


# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(null=True,blank=True)
    discount = models.FloatField(null=True,blank=True)# 请先检查discount_prices是否设置，discount_price存在的时候禁止设置discount
    pictures = models.CharField(max_length=800)#图片请按照存储名规则
    weight = models.IntegerField(default=1)
    introduction = models.TextField(blank=True)


class Img(models.Model):
    img_url = models.ImageField()
    img_info = models.CharField(max_length=420,blank=True)
    img_by = models.ForeignKey(to=Dish, on_delete=models.CASCADE)
