from django import forms
from django.contrib.auth.models import User


class userUpdate(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']