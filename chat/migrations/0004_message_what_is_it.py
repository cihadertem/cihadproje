# Generated by Django 3.2.4 on 2021-08-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210727_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='what_is_it',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
