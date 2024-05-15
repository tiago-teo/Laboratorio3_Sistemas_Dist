from django import forms 
  
# creating a form  
class RegisterForm(forms.Form): 
  
    username = forms.CharField(max_length = 200) 
    email = forms.CharField(widget = forms.EmailInput()) 
    password = forms.CharField(widget = forms.PasswordInput()) 

class LoginForm(forms.Form): 
  
    email = forms.CharField(widget = forms.EmailInput()) 
    password = forms.CharField(widget = forms.PasswordInput())


#class PackForm(forms.Form):
#
#    sender = forms.CharField(max_length = 100) 
#    receiver = forms.CharField(max_length = 100) 
#    name = forms.CharField(max_length = 100) 
#    description = forms.CharField(max_length = 300) 
#    sender_city = forms.CharField(max_length = 100) 
#    destination_city = forms.CharField(max_length = 100) 
#    tracking = forms.BooleanField()
#    status = forms.CharField(max_length = 100) 
