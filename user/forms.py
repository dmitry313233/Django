from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from catalog.forms import StileFormMixin
from user.models import User


# class LoginForm(StileFormMixin, AuthenticationForm):
#     pass


class UserRegisterForm(StileFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


# class UserVerificationForm(StileFormMixin, UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = '__all__'

class UserForm(UserChangeForm):
    pass
