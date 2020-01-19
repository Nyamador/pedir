from django.forms import ModelForm
from .models import Post


class BlogCreationForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Post
