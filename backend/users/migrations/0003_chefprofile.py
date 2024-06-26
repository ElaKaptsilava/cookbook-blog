# Generated by Django 5.0.4 on 2024-04-11 15:10

import django.db.models.deletion
import users.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChefProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to=users.models.user_directory_path)),
                ('image', models.ImageField(blank=True, null=True, upload_to=users.models.user_directory_path)),
                ('files', models.FileField(blank=True, null=True, upload_to=users.models.user_directory_path)),
                ('url', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
