# Generated by Django 5.0.2 on 2024-04-11 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_photo',
            field=models.URLField(max_length=500),
        ),
    ]
