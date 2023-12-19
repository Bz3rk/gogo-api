# Generated by Django 4.2.5 on 2023-12-19 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking_summary', '0003_ride_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
