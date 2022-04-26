from django import forms
from django.db.models import fields
from newsapp.models import AddReport, AdminLogin, RpLogin


class AddReportForm(forms.ModelForm):
    class Meta:
        model = AddReport
        fields = ('image', 'Title', 'Description','Type')
        widgets = { 
            "Title":  forms.TextInput(attrs={'autocomplete': 'off', 'class':"form-control"}), 
            "Description":  forms.TextInput(attrs={'autocomplete': 'off', 'class':"form-control"}),             
        }



class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = AdminLogin
        fields = ("username", "password")
        labels = {
            "username":"",
            "password":"",
        }
        widgets = { 
            "username":  forms.TextInput(attrs={'placeholder':'Admin Username','autocomplete': 'off', 'class':"form-control rounded-left"}), 
            "password": forms.PasswordInput(attrs={'placeholder':'Admin Password','autocomplete': 'off','data-toggle': 'password', 'class':"form-control rounded-left"}),
        }

class RpLoginForm(forms.ModelForm):
    class Meta:
        model = RpLogin
        fields = ("username", "password")
        labels = {
            "username":"",
            "password":"",
        }
        widgets = { 
            "username":  forms.TextInput(attrs={'placeholder':'Reporter Username','autocomplete': 'off', 'class':"form-control rounded-left"}), 
            "password": forms.PasswordInput(attrs={'placeholder':'Reporter Password','autocomplete': 'off','data-toggle': 'password', 'class':"form-control rounded-left"}),
        }

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = RpLogin
        fields = ("firstname", "lastname", "username", "password", "email", "contact", "image_url")
        labels = {
            "firstname":"",
            "lastname":"",
            "username":"",
            "password":"",
            "email":"",
            "contact":"",
            "image_url":"",
        }
        widgets = { 
            "firstname":  forms.TextInput(attrs={'placeholder':'Firstname','autocomplete': 'off', 'class':"form-control"}),
            "lastname":  forms.TextInput(attrs={'placeholder':'Lastname','autocomplete': 'off', 'class':"form-control"}),
            "username":  forms.TextInput(attrs={'placeholder':'Username','autocomplete': 'off', 'class':"form-control" ,'id': "userID" }), 
            "password": forms.PasswordInput(attrs={'placeholder':'Password','autocomplete': 'off','data-toggle': 'password', 'class':"form-control"}),
            "email":  forms.TextInput(attrs={'placeholder':'Email','autocomplete': 'off', 'class':"form-control", 'id':"Emailidverify"}),
            "contact":  forms.TextInput(attrs={'placeholder':'Contact','autocomplete': 'off', 'class':"form-control"}),
            

        }