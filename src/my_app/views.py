from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def homepage_view (request):
    return render(request, 'base.html')


