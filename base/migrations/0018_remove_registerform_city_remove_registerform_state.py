# Generated by Django 5.0.4 on 2024-05-01 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerform',
            name='City',
        ),
        migrations.RemoveField(
            model_name='registerform',
            name='State',
        ),
    ]
