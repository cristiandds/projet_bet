from django import forms
from .models import PetProfile, UserProfile, PetSitter
from django.contrib.auth.forms import UserChangeForm

class PetProfileForm(forms.ModelForm):
    class Meta:
        model = PetProfile
        fields = ['name', 'pet_type', 'breed', 'age', 'photo', 'bio', 'mating_available', 'for_adoption']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'phone', 'address']

class PetSitterForm(forms.ModelForm):
    class Meta:
        model = PetSitter
        fields = ['experience', 'photo', 'hourly_rate', 'services', 'location', 'country']
        widgets = {
            'experience': forms.Textarea(attrs={'rows': 4}),
            'services': forms.Textarea(attrs={'rows': 3}),
        }