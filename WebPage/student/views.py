from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterStudentForm
from .models import StudentProfile

def enterstudent(request):
	if request.method == 'POST':
		form = RegisterStudentForm(request.POST)
		if form.is_valid():
			student = form.save()
			return redirect('/liststudents')
	else:
		form = RegisterStudentForm()
	return render(request, 'student/enterstudent.html', {'form': form})

def liststudents(request):
	students = StudentProfile.objects.all().order_by('-name')
	return render(request, 'student/liststudents.html', {'students' : students})