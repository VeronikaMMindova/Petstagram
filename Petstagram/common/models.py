from django.db import models

from Petstagram.photos.models import PetPhoto


# Create your models here.
class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 30

    text = models.TextField(max_length=MAX_TEXT_LENGTH)

    created_at = models.DateTimeField(
        auto_now_add=True,  # done only on 'create'
    )
    modified_at = models.DateTimeField(
        auto_now=True,  # on every save
    )

    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.DO_NOTHING
    )

class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.DO_NOTHING
    )

# photo_like = PhotoLike.objects.filter(pet_photo_id=pet_photo.pk, user=request.user)