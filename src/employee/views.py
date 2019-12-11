from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EmpDetailForm

from .models import Employee

# Create your views here.
def emp_create_view(request):

	if request.method == 'POST':
		form = EmpDetailForm(request.POST)

		if form.is_valid():
			# form.save()
			Employee.objects.create(**form.cleaned_data)
			return HttpResponseRedirect('/')

	else:
		form = EmpDetailForm()

	context = {
		'form':form
	}
	return render(request, "employees/emp_detail_form.html", context)


def emp_details_view(request):
	employees = Employee.objects.all()
	context = {
		'employees':employees
	}
	return render(request, "employees/index.html", context)


def emp_update_view(request, emp_id):
	instance = Employee.objects.get(id=emp_id)
	form = EmpDetailForm(request.POST or None, instance=instance)
	if request.method == 'POST':
		if form.is_valid():
			# form.save()
			Employee.objects.update(**form.cleaned_data)
			return HttpResponseRedirect('/')

	context = {
		'form':form,
		'emp_id':emp_id
	}
	return render(request, "employees/emp_detail_form.html", context)


def emp_delete_view(request, emp_id):
	Employee.objects.get(id=emp_id).delete()
	return HttpResponseRedirect('/')
