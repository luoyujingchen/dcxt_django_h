# Generated by Django 2.1.1 on 2018-09-17 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcxt', '0004_auto_20180913_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to='')),
                ('img_info', models.CharField(blank=True, max_length=420)),
                ('img_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcxt.Dish')),
            ],
        ),
    ]