from django import forms
from .models import *

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
