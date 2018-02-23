from django import forms

__all__ = (
    'SignupForm',
)


class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput
    )
    # ckbox = forms.BooleanField()
    # any_thing = forms.ChoiceField()
