# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 09:01
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('enterpriseId', models.IntegerField(primary_key=True, serialize=False)),
                ('NEIType', models.CharField(max_length=255, null=True)),
                ('nameAbbreviation', models.CharField(max_length=255, null=True)),
                ('enterpriseName', models.CharField(max_length=255, null=True)),
                ('environmentAssessmentCompany', models.CharField(max_length=255, null=True)),
                ('corporateId', models.CharField(max_length=18, null=True)),
                ('corporateName', models.CharField(max_length=10, null=True)),
                ('contacts', models.CharField(max_length=10, null=True)),
                ('telephone', models.CharField(max_length=20, null=True)),
                ('postalCode', models.CharField(max_length=6, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('totalInvestment', models.IntegerField(null=True)),
                ('environmentalProtectionInvestment', models.IntegerField(null=True)),
                ('environmentalProtectionInvestmentProtection', models.FloatField(null=True)),
                ('floorSpace', models.IntegerField(null=True)),
                ('managementSpace', models.IntegerField(null=True)),
                ('nonAccommodationNum', models.IntegerField(null=True)),
                ('accommodationNum', models.IntegerField(null=True)),
                ('stuffNum', models.IntegerField(null=True)),
                ('dayWorkTime', models.IntegerField(null=True)),
                ('yearWorkTime', models.IntegerField(null=True)),
                ('investmentTime', models.IntegerField(null=True)),
                ('productNames', models.CharField(max_length=255, null=True)),
                ('constructionScale', models.CharField(max_length=50, null=True)),
                ('noiseEquipment', models.CharField(max_length=50, null=True)),
                ('noiseMonitoringPoints', models.IntegerField(null=True)),
                ('annualSolidWasteOutput', models.FloatField(null=True)),
                ('annualPowerConsumption', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longtitude', models.FloatField(null=True)),
                ('east', models.FloatField(null=True)),
                ('south', models.FloatField(null=True)),
                ('west', models.FloatField(null=True)),
                ('north', models.FloatField(null=True)),
                ('township', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productsId', models.IntegerField(primary_key=True, serialize=False)),
                ('productsName', models.CharField(max_length=50, null=True)),
                ('num', models.BigIntegerField(null=True)),
                ('unit', models.CharField(max_length=20, null=True)),
                ('enterpriseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EIA.Enterprise')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('enterpriseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EIA.Enterprise')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
