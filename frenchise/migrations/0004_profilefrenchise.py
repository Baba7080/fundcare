# Generated by Django 4.2.6 on 2023-10-09 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frenchise', '0003_rename_frenchise_frenchise_employee_register_model_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileFrenchise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frenchise_name', models.CharField(max_length=30)),
                ('Code', models.CharField(max_length=100)),
                ('DOB', models.DateField(max_length=8, null=True)),
                ('gender', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=100)),
                ('number', models.IntegerField(max_length=10)),
                ('Education', models.CharField(max_length=100)),
                ('Occupation', models.CharField(max_length=100)),
                ('Work_Type', models.CharField(max_length=20)),
                ('Address_Type', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
