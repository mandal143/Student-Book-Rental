# Generated by Django 5.1.1 on 2024-10-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='rented_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
