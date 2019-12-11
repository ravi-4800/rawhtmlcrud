from django import forms

from .models import Employee

class EmpDetailForm(forms.Form):
	name = forms.CharField()
	company_id = forms.CharField()
	age = forms.IntegerField()
	email = forms.CharField()
	location = forms.CharField()
	designation = forms.CharField()
	skill = forms.CharField()