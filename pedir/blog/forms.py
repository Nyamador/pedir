from django.forms import ModelForm
from .models import Blog


class BlogCreationForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Blog
