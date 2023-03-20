# Generated by Django 4.1.1 on 2023-03-20 20:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_profile', '0003_employee_profile_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]