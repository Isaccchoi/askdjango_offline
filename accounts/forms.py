from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
        #fields = ('username','email,)


def answer_validator(value):
    if value != 6:
        raise forms.ValidationError("땡!")


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='3 + 3 = ?', validators=[answer_validator])
