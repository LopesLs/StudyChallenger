from allauth.account.forms import SignupForm, LoginForm
from django import forms


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = forms.TextInput(attrs={"class": "input-form"})
        self.fields["email"].widget = forms.HiddenInput()
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "input-form"}
        )
        self.fields["password1"].help_text = ""
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "input-form"}
        )
        self.fields["password2"].help_text = ""


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget = forms.TextInput(attrs={"class": "input-form"})
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"class": "input-form mb-3"}
        )