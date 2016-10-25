from django import forms
 
from .models import UploadFile
 
 
class UploadFileForm(forms.ModelForm):
     
    class Meta:
        model = UploadFile
        fields = ['file']
        
class CroppingForm(forms.Form):

        top = forms.IntegerField(required=False)
        bottom = forms.IntegerField(required=False)
        left = forms.IntegerField(required=False)
        right = forms.IntegerField(required=False)
