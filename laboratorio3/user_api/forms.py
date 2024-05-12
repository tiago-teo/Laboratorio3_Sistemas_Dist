from django import forms 
  
# creating a form  
class RegisterForm(forms.Form): 
  
    username = forms.CharField(max_length = 200) 
    email = forms.CharField(widget = forms.EmailInput()) 
    password = forms.CharField(widget = forms.PasswordInput()) 

class LoginForm(forms.Form): 
  
    email = forms.CharField(widget = forms.EmailInput()) 
    password = forms.CharField(widget = forms.PasswordInput()) 