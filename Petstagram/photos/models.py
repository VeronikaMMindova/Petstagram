from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.pets.models import Pet

def validate_image_size_less_than_1mb(value):
    if value.size > SIZE_1_MB:
        raise ValueError("File size must be less than 1MB")


SIZE_1_MB = 1 * 1024 * 1024
# Create your models here.
class PetPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        blank=False,
        null=False,
        validators=(validate_image_size_less_than_1mb,)
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )
    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True,
    )

    pets = models.ManyToManyField(Pet)

    created_at = models.DateTimeField(
        auto_now_add=True, #done only on 'create'
    )
    modified_at = models.DateTimeField(
        auto_now=True,  #on every save
    )