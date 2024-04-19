# Generated by Django 4.0.5 on 2024-04-12 14:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='St18Independants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'sante"."st18_independants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='St19Cabinets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'sante"."st19_cabinets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='St22DoctorChangeSuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.TextField(choices=[('Unknown', 'Unknown'), ('Available', 'Available'), ('Not available', 'Not available'), ('Available with conditions', 'Available with conditions')], default='Unknown', verbose_name='availability')),
                ('comments', models.TextField(blank=True, verbose_name='comments')),
                ('requested_when', models.DateTimeField(default=django.utils.timezone.now, verbose_name='requested_when')),
                ('is_done', models.BooleanField(default=False, verbose_name='is_done')),
            ],
            options={
                'verbose_name': 'St22DoctorChangeSuggestion',
                'db_table': 'sante"."st22_doctor_change_suggestion',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='st21availabledoctorswithgeom',
            options={'managed': False, 'verbose_name': 'St21AvailableDoctorsWithGeom'},
        ),
    ]
