from django import forms


class Config(forms.Form):
        num_spots = forms.IntegerField(label="Number of conveyer spots?")
