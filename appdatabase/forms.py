from .models import User
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, BooleanField
from django import forms

class UserForm(ModelForm):
    in_group = BooleanField(required=True)
    moder = BooleanField(required=True)
    def clean_email(self):
            """
            Проверка email на уникальность
            """
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')
            if email and User.objects.filter(email=email).exclude(username=username).exists():
                raise forms.ValidationError('Email адрес должен быть уникальным')
            return email

    class Meta:
        model = User
        
        fields = ["name_user", "name_group","mail","password","year","name_university","name_specialization", "in_group","moder"]
        
        widgets = {
            "name_user": TextInput(attrs={
                'class': 'first',
                'placeholder': "  Фамилия Имя",
                'pattern':"\s",
                'style':"margin-top: 1%" }),
            "name_group": TextInput(attrs={
                'class': 'first',
                'placeholder': "  Код группы",
                'pattern':"\s",
                'style':"margin-top: 1%" }),
            "mail": EmailInput(attrs={
                'class': 'first',
                'placeholder': "  Почта",
                'style':"margin-top: 1%" }),
            "password": TextInput(attrs={
                'class': 'first',
                'placeholder': "  Пароль",
                'style':"margin-top: 1%" }),
            "year": NumberInput(attrs={
                'class': 'first',
                'placeholder': "  Год поступления",
                'style':"margin-top: 1%" }),
            "name_specialization": TextInput(attrs={
                'class': 'first',
                'placeholder': "  Специальность (в формате 2.09.03.02)",
                'style':"margin-top: 1%" }),
            "name_university": TextInput(attrs={
                'class': 'first',
                'placeholder': "  ВУЗ/СПО",
                'style':"margin-top: 1%" })
        }
