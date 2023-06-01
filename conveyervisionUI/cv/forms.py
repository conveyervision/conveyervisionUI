from django import forms
from cv.models import CVConfig


class Config(forms.Form):
    current_config = CVConfig.objects.first() # gets the first config
    num_spots = forms.IntegerField(label="Number of conveyer spots?",initial=current_config.num_spots)
