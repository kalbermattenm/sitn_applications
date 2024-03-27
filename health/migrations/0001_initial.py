# Generated by Django 4.0.5 on 2024-03-27 15:07

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='St21AvailableDoctorsWithGeom',
            fields=[
                ('availability', models.TextField(choices=[('Unknown', 'Unknown'), ('Available', 'Available'), ('Not available', 'Not available'), ('Available with conditions', 'Available with conditions')], default='Unknown', verbose_name='availability')),
                ('availability_conditions', models.TextField(blank=True, null=True, verbose_name='availability_conditions')),
                ('has_parking', models.BooleanField(null=True, verbose_name='has_parking')),
                ('has_disabled_access', models.BooleanField(null=True, verbose_name='has_disabled_access')),
                ('has_lift', models.BooleanField(null=True, verbose_name='has_lift')),
                ('spoken_languages', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None, verbose_name='spoken_languages')),
                ('is_rsn_member', models.BooleanField(null=True, verbose_name='is_rsn_member')),
                ('id_person_address', models.TextField(primary_key=True, serialize=False, verbose_name='id_person_address')),
                ('nom', models.TextField()),
                ('prenoms', models.TextField()),
                ('profession', models.TextField()),
                ('specialites', models.TextField()),
                ('notel', models.TextField(null=True)),
                ('address', models.TextField()),
                ('nopostal', models.TextField()),
                ('localite', models.TextField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=2056)),
            ],
            options={
                'db_table': 'sante"."st21_available_doctors_with_geom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='St20AvailableDoctors',
            fields=[
                ('availability', models.TextField(choices=[('Unknown', 'Unknown'), ('Available', 'Available'), ('Not available', 'Not available'), ('Available with conditions', 'Available with conditions')], default='Unknown', verbose_name='availability')),
                ('availability_conditions', models.TextField(blank=True, null=True, verbose_name='availability_conditions')),
                ('has_parking', models.BooleanField(null=True, verbose_name='has_parking')),
                ('has_disabled_access', models.BooleanField(null=True, verbose_name='has_disabled_access')),
                ('has_lift', models.BooleanField(null=True, verbose_name='has_lift')),
                ('spoken_languages', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None, verbose_name='spoken_languages')),
                ('is_rsn_member', models.BooleanField(null=True, verbose_name='is_rsn_member')),
                ('doctor', models.OneToOneField(db_column='id_person_address', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='health.st21availabledoctorswithgeom', verbose_name='doctor_nemedreg')),
                ('login_email', models.CharField(blank=True, max_length=255)),
                ('edit_guid', models.UUIDField(blank=True, null=True)),
                ('guid_requested_when', models.DateTimeField(blank=True, null=True)),
                ('last_edit', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'St20AvailableDoctors',
                'db_table': 'sante"."st20_available_doctors',
                'managed': False,
            },
        ),
    ]
