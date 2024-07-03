from django.shortcuts import render , redirect

# Create your views here.

def index(request):
    return render(request, 'theminimanagement/index.html')

def jobs(request):
    return render(request, 'theminimanagement/jobs.html')

def map(request):
    return render(request, 'theminimanagement/map.html')

def new_job(request):
    return render(request, 'theminimanagement/new_job.html')

def edit(request):
    return render(request, 'theminimanagement/edit.html')





