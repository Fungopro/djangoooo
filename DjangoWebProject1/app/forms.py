"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import SignUpModel
from app.models import UserNews
from ckeditor.fields import RichTextField


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        password = forms.CharField(label=_("Password"),
                                   widget=forms.PasswordInput({
                                       'class': 'form-control',
                                       'placeholder': 'Password'}))
        fields = ["username", "email", "password"]


class NewNews(forms.ModelForm):
    class Meta:
        model = UserNews

        art_title = forms.TextInput(attrs={'class': 'span17'}),
        art_text = RichTextField(blank=True, default=''),
        exclude = ['art_date', 'art_likes', 'art_active', 'art_author']


class SelectAnswer(forms.Form):
    ans_num = forms.CharField(label='Your name', max_length=100)