# Generated by Django 5.0.3 on 2024-03-19 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PetPhotos',
            new_name='PetPhoto',
        ),
    ]
