from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms






class SignUpForm(UserCreationForm):
    email = forms.EmailField(Label="", widget=forms.Textinput(attrs={'class':'form-control'), required=False})
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control':'first Name'})
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control':'first Name'})
    
    class Meta:
        model = User
        fields = ('username', 'subtitle', 'intro', 'body', 'conclusion', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'you must write a best hacking article...'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'conclusion': forms.Textarea(attrs={'class': 'form-control'}),