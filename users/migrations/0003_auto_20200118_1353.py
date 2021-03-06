# Generated by Django 2.2.6 on 2020-01-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default=1, upload_to='photos/%Y/%m/%d/', verbose_name='Profile Photo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='N/A', max_length=500, verbose_name='Bio'),
        ),
    ]
