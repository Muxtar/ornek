from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Username form',
        'class': 'form-control',
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Password form',
        'class': 'form-control'
    }))

    # def clean(self):
    #     return super().clean()
    

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Again Password'
    }))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

        widgets = {
            'username':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
        }


    def clean_password2(self):
        pass

    def save(self, *args, **kwargs):
        User.objects.create_user(
                            username = self.cleaned_data.get('username'),
                            first_name = self.cleaned_data.get('first_name'),
                            last_name = self.cleaned_data.get('last_name'),
                            email = self.cleaned_data.get('email'),
                            password = self.cleaned_data.get('password')
                            )
        # super().save(*args, **kwargs)