from django.db import models

# Create your models here.

class Employee(models.Model):
	emp_name=models.CharField(max_length=30)
	emp_id=models.IntegerField()
	designation=models.CharField(max_length=40)
	date_of_joining=models.DateTimeField()
	department=models.CharField(max_length=40)
	salary=models.IntegerField()
	experience=models.IntegerField() 

class Calender(models.Model):
	date=models.DateTimeField()
	occation=models.CharField(max_length=100)
	details=models.CharField(max_length=100)

class Latestnews(models.Model):
	details=models.CharField(max_length=100)