from django.shortcuts import render
from django.http import HttpResponse
def tasks(request):
    return HttpResponse("Main tasks page")
# Create your views here.
