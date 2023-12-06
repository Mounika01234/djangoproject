from django import forms
from empapp.models import Employee
from empapp.models import Calender
from empapp.models import Latestnews

class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields='__all__'

class CalenderForm(forms.ModelForm):
	class Meta:
		model=Calender
		fields='__all__'

class LatestnewsForm(forms.ModelForm):
	class Meta:
		model=Latestnews
		fields='__all__'