# Generated by Django 3.1.3 on 2022-02-10 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Resim')),
                ('type', models.CharField(max_length=20, verbose_name='Tür')),
                ('genius', models.CharField(max_length=20, verbose_name='Cins')),
                ('name', models.CharField(max_length=20, verbose_name='İsim')),
                ('age', models.CharField(max_length=4, verbose_name='Yaş')),
                ('explanation', models.TextField(verbose_name='Açıklama')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Katılma Tarihi')),
                ('petowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
