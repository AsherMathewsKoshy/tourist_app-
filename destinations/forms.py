# destinations/forms.py
from django import forms
from .models import Destination  # Make sure to import your Destination model

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['place_name', 'weather', 'country', 'state', 'district', 'description', 'image', 'location_link']
