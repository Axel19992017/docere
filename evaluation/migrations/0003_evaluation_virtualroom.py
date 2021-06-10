# Generated by Django 3.2.4 on 2021-06-10 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtualroom', '0003_auto_20210608_2002'),
        ('evaluation', '0002_auto_20210610_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='virtualroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='virtualroom.virtualroom', verbose_name='Clase'),
            preserve_default=False,
        ),
    ]