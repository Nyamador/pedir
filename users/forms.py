from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Profile
