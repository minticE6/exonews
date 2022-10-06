from django import forms
from .models import userandpassword

class Userandpasswordform(forms.ModelForm):
    class Meta:
        model = userandpassword
        fields = '__all__'
