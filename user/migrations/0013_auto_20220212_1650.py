# Generated by Django 3.1.3 on 2022-02-12 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_delete_meeting'),
        ('user', '0012_meeting_petowner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='pet',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='petowner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pet_petowner', to='pet.pet'),
        ),
    ]