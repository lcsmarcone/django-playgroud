# Generated by Django 5.2.4 on 2025-07-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0005_alter_car_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="cars/"),
        ),
    ]
