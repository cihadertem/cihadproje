# Generated by Django 3.2.4 on 2021-07-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthdate',
            field=models.DateTimeField(null=True),
        ),
    ]
