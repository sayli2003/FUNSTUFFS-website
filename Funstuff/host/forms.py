from django import forms
from .models import AddArt

class MyModelForm(forms.ModelForm):
    class Meta:
        model = AddArt
        fields = ('image','title','desp')
