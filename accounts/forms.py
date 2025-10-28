from django import forms
from .models import UserProfile


class RegisterForm(forms.ModelForm):
    
    date_of_birth = forms.DateField(
        widget = forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = UserProfile
        fields = [ 'user','date_of_birth', 'phone_number', 'weight', 'height', 'gender','blood_group']
