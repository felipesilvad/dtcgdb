from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile, UserCard
from cards.models import Card, Set

class userRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class Collection(forms.ModelForm):
    class Meta:
        model = UserCard
        fields = ['quantity', 'quantity_parallel', 'quantity_jp', 'quantity_parallel_jp']

class Collection_Set(forms.ModelForm):
    class Meta:
        model = UserCard
        fields = ['quantity', 'quantity_parallel', 'quantity_jp', 'quantity_parallel_jp', 'card']
        quantity = forms.IntegerField(widget=forms.HiddenInput())

        widgets = {
            'card': forms.TextInput()
        }