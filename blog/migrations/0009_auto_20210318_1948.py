# Generated by Django 3.1.6 on 2021-03-18 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210318_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m'),
        ),
    ]
