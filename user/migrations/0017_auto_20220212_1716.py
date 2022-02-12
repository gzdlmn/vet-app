# Generated by Django 3.1.3 on 2022-02-12 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_delete_meeting'),
        ('user', '0016_meeting_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='name',
        ),
        migrations.AddField(
            model_name='meeting',
            name='pet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pet.pet'),
        ),
    ]
