from django import forms
from django.contrib.auth.models import User
from pizzashopapp.models import PizzaShop,Pizza,ClentRole,TestModel


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','email')

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100,required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','email')


class PizzaShopForm(forms.ModelForm):
    class Meta:
        model = PizzaShop
        fields = ('name','phone','address','logo')


class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ('name', 'describtion', 'image', 'price')


class ClientRoleForm(forms.ModelForm):

    class Meta:
        model = ClentRole
        fields = ('user', 'role')


class TestModelForm(forms.ModelForm):


    class Meta:
        model = TestModel
        fields = ('user', 'rating', 'role')