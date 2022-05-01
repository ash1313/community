from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
class SignInForm(forms.Form):
    error_messages = {
        'user_missmatch': _('이메일 혹은 비밀번호를 다시 입력해주세요')
    }
    email = forms.EmailField(
        label=_("이름"),
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        label=_("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(
            attrs={'placeholder': '이메일'})
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'placeholder': '비밀번호'})
        self.fields['password'].widget.attrs['class'] = 'form-control'

    def clean(self):
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password1)
        if user is None:
            raise forms.ValidationError(
                self.error_messages['user_missmatch'],
                code='user_missmatch',
            )
        return self.cleaned_data

    def get_user(self):
        return self.user