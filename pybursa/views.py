#from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	#return render(request, "index.html")
	return render(request, 'index.html')

def contact(request):
	#return render(request, "contact.html") 
	return render(request, 'contact.html')

def student_list(request):
	#return render(request, "student_list.html")
	return render(request, 'student_list.html')

def student_detail(request):
	#return render(request, "student_detail.html") 
	return render(request, 'student_detail.html')