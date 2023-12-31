# Generated by Django 4.2.1 on 2023-06-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_ip_address_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_level',
            field=models.CharField(choices=[('admin', 'Admin'), ('engineer', 'Engineer'), ('manager', 'Manager'), ('supervisor', 'Supervisor'), ('user', 'User'), ('applicant', 'Applicant')], default='applicant', max_length=50),
        ),
    ]
