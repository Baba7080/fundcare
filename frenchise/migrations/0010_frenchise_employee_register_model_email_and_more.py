# Generated by Django 4.2.4 on 2023-10-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frenchise', '0009_rename_employee_name_frenchise_employee_register_model_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='frenchise_employee_register_model',
            name='email',
            field=models.EmailField(default='employee@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='frenchise_employee_register_model',
            name='employee_id',
            field=models.IntegerField(default=123456),
        ),
        migrations.AlterField(
            model_name='frenchise_employee_register_model',
            name='username',
            field=models.CharField(default='Username', max_length=15),
        ),
    ]
