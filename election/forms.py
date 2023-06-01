
from django import forms
from .models import Location, Category, Evidence

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EvidenceForm(forms.ModelForm):
    
    class Meta:
         model =Evidence
         fields = ('evidence','happened_on','description','location','category','reporter')
    
       
        
    def clean_field(self):
         data = self.cleaned_data('fields') 



class Category(forms.ModelForm):

    class Meta:
        model=Category
        fields=('__all__')
    def clean_field(self):
        data=self.cleaned_data('fields')


class LocationForm(forms.ModelForm):
    

    class Meta:
        model =Location
        fields = ('__all__')
    def clean_field(self):
        data = self.cleaned_data('fields') 


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user  
