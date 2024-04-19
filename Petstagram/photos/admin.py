from django.contrib import admin

from Petstagram.photos.models import PetPhoto


# Register your models here.
@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'location', 'created_at','short_description', 'tagged_pets')

    def short_description(self, obj):
        return obj.description[:15]

    def tagged_pets(self, obj):
        return ', '.join(pet.name for pet in obj.pets.all())