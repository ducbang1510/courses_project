# Generated by Django 3.2.6 on 2021-08-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210720_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='static/courses/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(default=None, upload_to='static/courses/%Y/%m'),
        ),
    ]