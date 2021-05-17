# Generated by Django 3.2.3 on 2021-05-17 08:28

from django.db import migrations, models
import user.formatchecker


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('username', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birthday', models.DateField(blank=True, default=None, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=16)),
                ('phone', models.CharField(max_length=64, unique=True)),
                ('country', models.CharField(blank=True, max_length=128, null=True)),
                ('state', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('avatar', user.formatchecker.ContentTypeRestrictedFileField(blank=True, null=True, upload_to='users/uploads/%Y/%m/%d/')),
                ('is_banned', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_vlad', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
