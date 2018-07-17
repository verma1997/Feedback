from django import forms
from MyApp.models import UserProfile

class NewUserProfile(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = '__all__'
