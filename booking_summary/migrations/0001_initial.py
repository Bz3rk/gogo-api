# Generated by Django 4.2.5 on 2023-11-23 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_location', models.CharField(max_length=300)),
                ('destination', models.CharField(max_length=300)),
                ('two_way', models.BooleanField()),
                ('no_of_passengers', models.IntegerField()),
                ('pickup_long', models.FloatField()),
                ('pickup_lat', models.FloatField()),
                ('dest_long', models.FloatField()),
                ('dest_lat', models.FloatField()),
                ('distance', models.FloatField()),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Junction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_passengers', models.IntegerField(default=1)),
                ('two_way', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end_junction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='end_junction', to='booking_summary.junction')),
                ('start_junction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='start_junction_rides', to='booking_summary.junction')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
