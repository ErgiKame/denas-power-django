from django import forms
from .models import User

class UserCreateForm(forms.ModelForm):
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
        )
