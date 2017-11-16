from django import forms
from .models import Enterprise, User


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['enterpriseName']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'telephone', 'email', 'password', 'is_manager','environmentAssessmentCompany']
