# Generated by Django 3.1.3 on 2022-02-12 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20220212_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='petowner',
        ),
    ]
