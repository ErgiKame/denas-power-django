from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'   <------ Use this for all fields
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'is_admin',
            'password1',
            'password2',
        )
        def save(self, commit=True):
            user = super(UserCreateForm, self).save(commit=False)
            if commit:
                user.save()
            return user
