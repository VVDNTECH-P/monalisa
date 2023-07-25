from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField
from django.contrib.auth.models import User


from .models import admin_post
class admin_form(forms.ModelForm):
    class Meta :
        model = admin_post
        fields = [ 'image']

    
        widgets= {'title':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Title'}),
}
        error_messages={
                    'image': { 'required' : 'please select an image'},
        }
        
        

class signup_form (UserCreationForm) :
        password1=forms.CharField(error_messages={'required':'Enter password'} , label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        password2=forms.CharField(error_messages={'required':'Enter password again'} , label='Password(again)',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        class Meta:
            model = User
            fields = ['username','first_name','last_name','email']

            labels= {'first_name' : 'First Name',
                    'last_name'  : 'Last Name',
                    'email'      : 'Email' , 
    
            

                }
            widgets= {'username':forms.TextInput(attrs={'class': 'form-control'}),
                    'last_name':forms.TextInput(attrs={'class': 'form-control'}),
                    'first_name':forms.TextInput(attrs={'class': 'form-control'}),
                    'email':forms.EmailInput(attrs={'class': 'form-control'}),


            }
            error_messages={
                    'username' : { 'required' : 'please enter title '},
        }
        

class user_logedin_form(AuthenticationForm):
    username=UsernameField(error_messages={'required':'Enter username'} , widget=forms.TextInput( attrs={'autofocus':True ,'class': 'form-control','placeholder' : 'Enter Username' }))
    password=forms.CharField(error_messages={'required':'Enter password'} ,strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-possword' ,'class': 'form-control','placeholder' : 'Enter Password' }))

    