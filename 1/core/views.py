from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Main core page")

# Create your views here.
