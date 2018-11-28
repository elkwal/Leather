from django import forms
from .models import User_profile



class UploadForm(forms.ModelForm):
    
    class Meta:
     
        exclude = ['user','profile']
