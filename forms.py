from django import forms
from .models import *

class Userform(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Multiple
        fields = "__all__"
