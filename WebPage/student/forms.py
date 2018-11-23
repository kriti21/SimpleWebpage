from django import forms
from django.forms import ModelForm
from student.models import StudentProfile

class RegisterStudentForm(ModelForm):

	class Meta:
		model = StudentProfile
		fields = {'name', 'age', 'gender',}
