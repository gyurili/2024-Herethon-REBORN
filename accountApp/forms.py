import re

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.forms import Textarea

from .models import User


class AccountCreationForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': '아이디 (이메일 형식)'})
    )
    nickname = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(attrs={'placeholder': '닉네임'})
    )
    image = forms.ImageField(
        label='Profile Image',
        required=False,
        widget=forms.FileInput()
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 (영어, 숫자, 특수문자 조합 12자 이상)'})
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 재확인'})
    )

    class Meta:
        model = User
        fields = ('email', 'nickname', 'image')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+~`|}{[\]:;?><,./\-\\]).{12,}$', password1):
                raise forms.ValidationError(
                    "Password must be at least 12 characters long and contain letters, numbers, and special characters."
                )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'nickname', 'image',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if not password:
            user.password = self.initial["password"]  # 기존 비밀번호 유지
        if commit:
            user.save()
        return user


class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '아이디'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호'})
    )