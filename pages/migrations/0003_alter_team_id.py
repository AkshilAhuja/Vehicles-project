# Generated by Django 4.0 on 2024-05-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20240514_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
