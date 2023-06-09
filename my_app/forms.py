from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', max_length=100, widget = forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder':
        ' Enter Email'}))
    first_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                     'placeholder':
        'Enter First Name'}))
    last_name = forms.CharField(label='',max_length=100, widget= forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder':'Enter Last '
                                                                                                      'Name'}))

    # meta class to specify the model and fields to use
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # override the constructor to customize field widgets and labels
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # customize the username field widget
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        # customize the password1 field widget
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        # customize the password2 field widget
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'



class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs={'class':
                                                                                                        'form-control',
                                                                                    'placeholder':
        ' Enter First Name'}))
    last_name = forms.CharField(required=True, label = '',widget = forms.TextInput(attrs={'class':
                                                                                                      'form-control',
                                                                                    'placeholder':
        ' Enter Last Name'}))
    email = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder':
        ' Enter Email'}))
    address = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs={'class':
    'form-control',
                                                                                    'placeholder':
        ' Enter Address'}))
    zip_code = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs={'class':
                                                                                                      'form-control',
                                                                                    'placeholder':
        ' Enter zip code'}))
    country = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs={'class':
                                                                                                     'form-control',
                                                                                    'placeholder':
        ' Enter Country'}))
    city = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder':
        ' Enter City'}))

    class Meta:
        model = Customer
        exclude = ('user',)
