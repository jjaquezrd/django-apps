from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.models import User
from . import models

class EnquiryForm(forms.ModelForm):
    class Meta:
        model=models.Enquiry
        fields=('full_name', 'email','detail')
        
class SignUp(UserCreationForm):
    class Meta:
        model= User
        fields=('first_name','last_name','email','username','password1','password2')
        
class ProfileForm(UserChangeForm):
    class Meta:
        model= User
        fields=('first_name','last_name','email','username')
        
class TrainerLoginForm(forms.ModelForm):
    class Meta:
        model= models.Trainer
        fields=('username','pwd')
        
        widgets = {
           'pwd': forms.PasswordInput(),
        }

class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model= models.Trainer
        fields=('full_name','mobile','address','detail','img')

class TrainerChangePassword(forms.Form):
    new_password=forms.CharField(widget=forms.PasswordInput, required=True)
    


#class AttendanceForm(forms.ModelForm):
    #class Meta:
        #model= models.Attendance
        


        

        



    
        