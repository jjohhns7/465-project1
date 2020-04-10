from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def tasks(request):
    request_args = request.GET
    request_args_string = request_args.urlencode()
    page_data = {"args": request_args_string}
    return render(request, 'tasks/tasks.html', context=page_data)
# Create your views here.
