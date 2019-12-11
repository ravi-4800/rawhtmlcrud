from django.shortcuts import render
from django.http import HttpResponseRedirect

# from .forms import EmpDetailForm

from .models import Employee

# Create your views here.
def emp_create_view(request):
	emp = Employee()
	if(request.method == 'POST'):
		emp.name        = request.POST.get('name')
		emp.company_id  = request.POST.get('company_id')
		emp.age         = request.POST.get('age')
		emp.email       = request.POST.get('email')
		emp.location    = request.POST.get('location')
		emp.designation = request.POST.get('designation')
		emp.skill       = request.POST.get('skill')

		emp.save()
		return HttpResponseRedirect('/')
	context = {
		'emp': emp
	}
	return render(request, "employees/emp_detail_form.html", context)


def emp_details_view(request):
	employees = Employee.objects.all()
	context = {
		'employees':employees
	}
	return render(request, "employees/index.html", context)


def emp_update_view(request, emp_id):
	emp = Employee.objects.get(id=emp_id)
	if(request.method == 'POST'):
		emp.name        = request.POST.get('name')
		emp.company_id  = request.POST.get('company_id')
		emp.age         = request.POST.get('age')
		emp.email       = request.POST.get('email')
		emp.location    = request.POST.get('location')
		emp.designation = request.POST.get('designation')
		emp.skill       = request.POST.get('skill')

		emp.save()
		return HttpResponseRedirect('/')
	context = {
		'emp':emp,
		'emp_id':emp_id
	}
	return render(request, "employees/emp_detail_form.html", context)


def emp_delete_view(request, emp_id):
	Employee.objects.get(id=emp_id).delete()
	return HttpResponseRedirect('/')
