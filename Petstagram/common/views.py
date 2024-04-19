from django.shortcuts import render, redirect
from django.views import generic as views

from Petstagram.common.models import PhotoLike
from Petstagram.photos.models import PetPhoto


# Create your views here.
# def index(request):
#     context = {
#         'pet_photos': PetPhoto.objects.all(),
#     }
#     return render(request, 'common/index.html', context)
class IndexView(views.ListView):
    queryset = PetPhoto.objects.all()
    template_name = 'common/index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_by_pet_name_pattern(queryset)

        return queryset

    def filter_by_pet_name_pattern(self, queryset):
        return queryset.filter()

def like_pet_photo(request, pk):
    # pet_photo = PetPhoto.objects.get(pk=pk, user=request.user)
    pet_photo_like = PhotoLike.objects \
                      .filter(pet_photo_id=pk)\
                      .first()
    # dislike
    if pet_photo_like:
        pet_photo_like.delete()
    else:
        PhotoLike.objects.create(pet_photo_id=pk)
    return redirect(request.META.get('HTTP_REFERER') + f'#photo-{pk}')