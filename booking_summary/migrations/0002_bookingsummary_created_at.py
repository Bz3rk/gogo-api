# Generated by Django 4.2.5 on 2023-10-16 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking_summary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingsummary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
