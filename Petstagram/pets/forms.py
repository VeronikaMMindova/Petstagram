from django import forms
from django.core.exceptions import ValidationError

from Petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'pet_photo')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'pet_photo': forms.URLInput(attrs={'placeholder': 'Link to image'})
        }
        labels = {
            'name': 'Pet name',
            'pet_photo': 'Link to image'
        }

class PetCreateForm(PetBaseForm):
    pass

class ReadOnlyFieldsFormMixin:
    def _apply_readonly_fields(self):
        readonly_fields = "__al__"
class PetEditForm(ReadOnlyFieldsFormMixin, PetBaseForm):
    readonly_fields = ("date_of_birth",)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_fields()

    def clean_date_of_birth(self):
        # date_of_birth = self.cleaned_data['date_of_birth']
        # if date_of_birth != self.instance.date_of_birth:
        #     raise ValidationError('Date of birth is readonly')

        return self.instance.date_of_birth

class PetDeleteForm(ReadOnlyFieldsFormMixin, PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_fields()
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
