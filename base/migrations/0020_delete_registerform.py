# Generated by Django 5.0.4 on 2024-05-01 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_rename_address_registerform_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registerform',
        ),
    ]
