from django import forms
 
from .models import UploadFile
 
#from django.contrib.auth.forms import AuthenticationForm
class UploadFileForm(forms.ModelForm):
     
    class Meta:
        model = UploadFile
        fields = ['file']
