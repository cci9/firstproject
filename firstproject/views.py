from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request,'home.html',{'greeting':'Hey, whats up!'})

def about(request):
	return HttpResponse('Chetan About')