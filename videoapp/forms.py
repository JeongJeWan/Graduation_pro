from django.forms import ModelForm

from videoapp.models import Video


class Video_form(ModelForm):

    class Meta:
        model = Video
        fields = ['caption', 'video']
