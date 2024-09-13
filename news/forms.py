# from django.contrib.auth.models import User
from django import forms

from .models import News, Category, Comment, User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'rasm']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'rasm', 'username', 'email']

class PasswordForm(forms.Form):
    eski_password = forms.CharField(max_length=15)
    yangi_password = forms.CharField(max_length=15)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'rasm', 'tur']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['izoh']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

