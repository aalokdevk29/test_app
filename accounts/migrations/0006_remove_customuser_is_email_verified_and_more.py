# Generated by Django 4.2.10 on 2024-03-06 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_otp_delete_otpdevice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_email_verified',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='otp',
        ),
    ]
