from django import forms
from cv.models import CVConfig

class Config(forms.Form):
    num_spots = forms.IntegerField(label="Number of conveyer spots?")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_config = CVConfig.objects.first()  # gets the first config
        if current_config:
            self.fields['num_spots'].initial = current_config.num_spots

