import json
from django.shortcuts import render
import os
from django.conf import settings
# Create your views here.

def index(request):
    file_path = os.path.join(settings.BASE_DIR, 'theminimanagement', 'static', 'js', 'main_chart.json')
    with open(file_path, 'r') as file:
        chart_data = json.load(file)


    total_sum = sum(chart_data['datasets'][0]['data'])

    combined_data = []
    for i in range(len(chart_data['labels'])):
        value = chart_data['datasets'][0]['data'][i]
        percentage = (value / total_sum) * 100

        combined_data.append((chart_data['labels'][i], percentage))
    
    return render(request, 'theminimanagement/index.html', {
        'combined_data': combined_data,
        'chart_data': json.dumps(chart_data)
    })

def jobs(request):
    return render(request, 'theminimanagement/jobs.html')

def map(request):
    return render(request, 'theminimanagement/map.html')

def new_job(request):
    return render(request, 'theminimanagement/new_job.html')

def edit(request):
    return render(request, 'theminimanagement/edit.html')