from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from empapp.models import Employee
from empapp.forms import EmployeeForm
from empapp.models import Calender
from empapp.forms import CalenderForm
from empapp.models import Latestnews
from empapp.forms import LatestnewsForm
import csv
from django.http import HttpResponse


# Create your views here.

def homeview(request):
	return render(request,'empapp/home.html')

@login_required
def hrview(request):
	return render(request,'empapp/hr.html')

def employeeview(request):
	return render(request,'empapp/employee.html')

def updateview(request):
	return render(request,'empapp/update.html')

def empview(request):
	emp=Employee.objects.all()
	return render(request,'empapp/emp.html',{'e':emp})

def edataview(request):
	form=EmployeeForm()
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/emp')
	return render(request,'empapp/edata.html',{'form':form})

def deleteview(request,id):
	emp=Employee.objects.get(id=id)
	emp.delete()
	return redirect('/emp')

def updateview(request,id):
	emp=Employee.objects.get(id=id)
	form=EmployeeForm()
	if request.method=="POST":
		form=EmployeeForm(request.POST, instance=emp)
		if form.is_valid():
			form.save()
			return redirect('/emp/')
	return render(request,'empapp/update.html',{'e':emp})

def holidayview(request):
	calender=Calender.objects.all()
	return render(request,'empapp/holiday.html',{'c':calender})

def calenderview(request):
	form=CalenderForm()
	if request.method=="POST":
		form=CalenderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/holiday')
	return render(request,'empapp/calender.html',{'form':form})

def latestnewsview(request):
	latest=Latestnews.objects.all()
	return render(request,'empapp/latest.html',{'l':latest})

def newsview(request):
	form=LatestnewsForm()
	if request.method=="POST":
		form=LatestnewsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/latest')
	return render(request,'empapp/news.html',{'form':form})

def getfile(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="empdata.csv"'
	employees= Employee.objects.all()
	writer=csv.writer(response)
	writer.writerow(['EMP NAME','EMP ID','DESIGNATION','DATE OF JOINING','DEPARTMENT','SALARY','EXPERIENCE'])
	for m in employees:
		writer.writerow([m.emp_name,m.emp_id,m.designation,m.date_of_joining,m.department,m.salary,m.experience])
	return response
