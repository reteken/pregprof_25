from django import forms 
from .models import req

class ReqForm(forms.ModelForm):
    class Meta:
        model = req
        fields = ['req']
        widgets = {
            'req': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            })}