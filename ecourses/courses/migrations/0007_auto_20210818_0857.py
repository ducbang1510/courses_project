# Generated by Django 3.2.6 on 2021-08-18 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20210817_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='courses/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(default=None, upload_to='courses/%Y/%m'),
        ),
    ]
