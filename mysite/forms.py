from django import forms

from .models import UserData


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ('user_name', 'user_id', 'user_pwd',)
