# Generated by Django 3.0.7 on 2024-06-05 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_rename_is_feartured_car_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
