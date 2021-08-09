# Generated by Django 3.2.4 on 2021-08-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='klasikpp.jpg', null=True, upload_to='', verbose_name='Profil Resmi'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.CharField(blank=True, default='Henüz bir biyografi girilmedi...', max_length=1000, null=True, verbose_name='Biyografi'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(blank=True, default='2000-01-01', null=True, verbose_name='Doğum Tarihi'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadin'), ('Belirtilmedi', 'Belirtilmedi')], default='Belirtilmedi', max_length=100, null=True, verbose_name='Cinsiyet'),
        ),
    ]
