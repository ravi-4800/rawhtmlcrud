from django.db import models

class Employee(models.Model):
	name        = models.CharField(max_length=100)
	company_id  = models.CharField(max_length=30)
	age         = models.DecimalField(max_digits=3,decimal_places=0)
	email       = models.EmailField(max_length=30)
	location    = models.CharField(max_length=30)
	designation = models.CharField(max_length=30)
	skill       = models.CharField(max_length=30)
