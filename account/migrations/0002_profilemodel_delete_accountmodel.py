# Generated by Django 5.0.6 on 2024-05-11 06:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=150, null=True, verbose_name='username')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('fullname', models.CharField(blank=True, max_length=150, null=True, verbose_name='fullname')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='phone')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='position')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='address')),
                ('twitter', models.CharField(blank=True, max_length=250, null=True, verbose_name='twitter')),
                ('instagram', models.CharField(blank=True, max_length=250, null=True, verbose_name='instagram')),
                ('facebook', models.CharField(blank=True, max_length=250, null=True, verbose_name='facebook')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'userprofile',
                'verbose_name_plural': 'userprofile',
            },
        ),
        migrations.DeleteModel(
            name='AccountModel',
        ),
    ]
