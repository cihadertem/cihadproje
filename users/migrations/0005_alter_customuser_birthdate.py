# Generated by Django 3.2.4 on 2021-07-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]