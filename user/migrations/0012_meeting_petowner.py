# Generated by Django 3.1.3 on 2022-02-12 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_meeting_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='petowner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.petowner'),
        ),
    ]