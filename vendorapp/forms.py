from django import forms
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from .models import Multivendors, Fooditems


class VendorUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class MultivendorsForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Multivendors
        fields = [
            'restaurant_name', 'address', 'city', 'state', 'zip_code',
            'restaurant_lic', 'restaurant_img'
        ]
class UserregForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class FooditemsForm(forms.ModelForm):
    class Meta:
        model = Fooditems
        fields = ['item_name', 'item_desc', 'item_price', 'item_img']
        widgets = {
            'item_desc': forms.Textarea(attrs={'rows': 4}),
        }
        
class CartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    captcha = ReCaptchaField()
    class Meta:
        fields = ['quantity']