# Generated by Django 3.2.4 on 2021-08-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default='1', verbose_name='Fiyat'),
        ),
    ]