from django import forms
from .models import Shout, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UploadedImage

# Profile picture form


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture")
    profile_bio = forms.CharField(
        label="Profile Info", widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Profile Info'}))
    facebook_link = forms.CharField(
        label="Facebook Link", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Facebook Link'}))
    instagram_link = forms.CharField(
        label="Instagram Link", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Instagram Link'}))
    linkedin_link = forms.CharField(
        label="Linkedin Link", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Linkedin Link'}))
    youtube_link = forms.CharField(
        label="Youtube Link", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Youtube Link'}))
    x_link = forms.CharField(
        label="X Link", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'X Link'}))

    class Meta:
        model = Profile
        fields = (
                  'profile_image',
                  'profile_bio',
                  'facebook_link',
                  'instagram_link', 'linkedin_link', 'youtube_link', 'x_link',)

# Shout form


class ShoutForm(forms.ModelForm):
    body = forms.CharField(
        required=True, widget=forms.widgets.Textarea(
         attrs={
                "placeholder": "Enter your Shouts in The Saloon! ",
                "class": "form-control",
                }
                ),
        label="",
        )


class Meta:
    model = Shout
    exclude = ("user", "likes",)

# Sign up form


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(
        label="", max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        label="", max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text \
                                text-muted"><small></small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text \
                                text-muted"><small></small></span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm \
                                                                Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text \
                                    text-muted"><small></small></span>'


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ('image',)
