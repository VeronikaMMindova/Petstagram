from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from Petstagram.pets.models import Pet
from Petstagram.pets.forms import PetCreateForm, PetEditForm, PetBaseForm, PetDeleteForm


class PetCreateView(views.CreateView):
    form_class = PetCreateForm
    template_name = 'pets/create_pet.html'

    def get_success_url(self):
        return reverse('details pet', kwargs={
            'username': 'Veronika',
            'pet_slug': self.object.slug,
        })


class PetEditView(views.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/edit_pet.html'

    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['username'] = 'Veronika'
        return context

    def get_success_url(self):
        return reverse('details pet', kwargs={
            'username': self.request.GET.get('username'),
            'pet_slug': self.object.slug,

        })

class PetDetailView(views.DetailView):
    # model = Pet
    queryset = Pet.objects.all() \
            .prefetch_related("petphoto_set")
    template_name = "pets/details_pet.html"
    slug_url_kwarg = "pet_slug"

class PetDeleteView(views.DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/delete_pet.html'

    slug_url_kwarg = "pet_slug"
    success_url = reverse_lazy('index')

    extra_context = {
        'username': 'Veronika',
    }
#
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
