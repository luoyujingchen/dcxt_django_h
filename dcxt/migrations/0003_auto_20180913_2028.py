# Generated by Django 2.1.1 on 2018-09-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcxt', '0002_auto_20180913_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='discount_price',
            field=models.FloatField(default=models.FloatField()),
        ),
    ]
