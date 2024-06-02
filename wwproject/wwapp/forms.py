from django import forms
from django.contrib.auth.models import User
from wwapp.models import CarBooking,CarCategory,UserPersonalInfo,BlogModels,UserMessagesModel,LocationsModel

class UserRrgisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        widgets={
        'first_name':forms.TextInput(attrs={'class':'form-control bg-transparent','placeholder':'Firstname',}),
        'last_name':forms.TextInput(attrs={'class':'form-control bg-transparent','placeholder':'Lastname'}),
        'username':forms.TextInput(attrs={'class':'form-control bg-transparent','placeholder':'Username'}),
        'email':forms.EmailInput(attrs={'class':'form-control bg-transparent','placeholder':'Email'}),
        'password':forms.PasswordInput(attrs={'class':'form-control bg-transparent','placeholder':'Password'})
        } 


        
class CarBookingForm(forms.ModelForm):
    class Meta:
        model=CarBooking
        exclude=['user','total','name','price']
        # fields=['renter','place','contact','duration','color']
        widgets={
            'renter':forms.TextInput(attrs={'class':'form-control'}),
            'place':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'duration':forms.NumberInput(attrs={'class':'form-control w-50','placeholder':'day'}),
            'pd':forms.TextInput(attrs={'class':'form-control','type':'date'})
        }
        
class CarEditForm(forms.ModelForm):
    class Meta:
        model=CarCategory
        fields='__all__'
        
class UserPersonalInfoForm(forms.ModelForm):
    class Meta:
        model=UserPersonalInfo
        exclude=['user']
        # fields=['name','place','city','state','phone','dob','status','gender']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),
            'place':forms.TextInput(attrs={'class':'form-control','placeholder':'Place'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'dob':forms.TextInput(attrs={'class':'form-control','type':'date'}),
        }
class BlogForm(forms.ModelForm):
    class Meta:
        model=BlogModels
        exclude=['user']
        # fields="__all__"
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control m-2'}),
        }
        
class UserMessageForm(forms.ModelForm):
    class Meta:
        model=UserMessagesModel
        exclude=['user']
        widgets={
            'fname':forms.TextInput(attrs={'class':'form-control  w-50 float-start','placeholder':'Full Name'}),
            'email':forms.TextInput(attrs={'class':'form-control  w-50 float-start','placeholder':'Email'}),
            'message':forms.Textarea(attrs={'class':'form-control ','placeholder':'Message'})
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model=LocationsModel
        fields='__all__'
        widgets={
            'link':forms.TextInput(attrs={'class':'form-control ','placeholder':'Link'}),
            'area':forms.TextInput(attrs={'class':'form-control','placeholder':'Area'})
        }
class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
        }