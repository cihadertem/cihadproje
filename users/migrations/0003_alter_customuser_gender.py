# Generated by Django 3.2.4 on 2021-07-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210707_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadin')], max_length=100, null=True),
        ),
    ]
