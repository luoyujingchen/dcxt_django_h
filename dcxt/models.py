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