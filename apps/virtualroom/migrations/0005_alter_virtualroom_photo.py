# Generated by Django 3.2.6 on 2021-08-27 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualroom', '0004_auto_20210824_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualroom',
            name='photo',
            field=models.ImageField(upload_to='media/virtualrooms/', verbose_name='Foto'),
        ),
    ]