# Generated by Django 3.2.4 on 2021-06-10 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('virtualroom', '0003_auto_20210608_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(editable=False)),
                ('last_modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Descripción')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Puntuation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(editable=False)),
                ('last_modified', models.DateTimeField(editable=False)),
                ('amount', models.IntegerField(verbose_name='Cantidad')),
                ('observation', models.CharField(blank=True, max_length=150, verbose_name='Observaciones')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtualroom.enrollment', verbose_name='Inscripción del estudiante')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluation', verbose_name='Evaluación')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='evaluation',
            name='enrollments',
            field=models.ManyToManyField(through='evaluation.Puntuation', to='virtualroom.Enrollment', verbose_name='Estudiantes'),
        ),
    ]
