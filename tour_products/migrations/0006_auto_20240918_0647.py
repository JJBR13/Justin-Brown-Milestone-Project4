# Generated by Django 3.2.18 on 2024-09-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_products', '0005_auto_20240918_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourproducts',
            name='location_end',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tourproducts',
            name='location_start',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tourproducts',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='TourImage',
        ),
    ]
