import json
from django.shortcuts import render, redirect
import os
from django.conf import settings
# Create your views here.

def index(request):
    #here I am loading the data from the josn file: main_chart.json
    file_path = os.path.join(settings.BASE_DIR, 'theminimanagement', 'static', 'js', 'main_chart.json')
    with open(file_path, 'r') as file:
        chart_data = json.load(file)

    total_sum = sum(chart_data['datasets'][0]['data']) # here I am getting to total/sum of the data to later create the percetage

    combined_data = []
    for i in range(len(chart_data['labels'])):
        value = chart_data['datasets'][0]['data'][i]
        percentage = (value / total_sum) * 100

        combined_data.append((chart_data['labels'][i], percentage))
    #here I am loading the data from the josn file: job_data.json
    file_path_two = os.path.join(settings.BASE_DIR, 'theminimanagement', 'static', 'js', 'job_data.json')
    with open(file_path_two, 'r') as file:
        chart_data_two = json.load(file)

    job_names = []
    job_pro = []

    for i in range(len(chart_data_two['jobs'])):
        job_name = chart_data_two['jobs'][i]['labels']
        job_progress = chart_data_two['jobs'][i]['data']
        job_names.append(job_name)
        job_pro.append(job_progress)
        print(job_names, job_pro)
    
    return render(request, 'theminimanagement/index.html', {
        'job_names': job_names,
        'job_pro': job_pro,
        'combined_data': combined_data,
        'chart_data': json.dumps(chart_data)
    })

def jobs(request):
    #here I am loading the data from the josn file: job_data.json
    file_path = os.path.join(settings.BASE_DIR, 'theminimanagement', 'static', 'js', 'job_data.json')
    with open(file_path, 'r') as file:
        data = json.load(file)

    jobs = data.get('jobs', [])

    return render(request, 'theminimanagement/jobs.html', {'jobs': jobs})

def map(request):
    return render(request, 'theminimanagement/map.html')

def new_job(request):
    if request.method == 'POST':
        job_name = request.POST.get('name')
        job_street = request.POST.get('address')
        job_town = request.POST.get('town')
        job_post_code = request.POST.get('post-code')

        job_address = job_street + "," + " " + job_town + " " + job_post_code

        

        file_path_three = os.path.join(settings.BASE_DIR, 'theminimanagement', 'static', 'js', 'job_data.json')
        with open(file_path_three, 'r+') as file:
            data_add_job = json.load(file)

            id = len(data_add_job['jobs']) + 1

            print(id)

            new_job = {"id": id,"labels": job_name, "address": job_address, "data": "0"}

            data_add_job['jobs'].append(new_job)
            file.seek(0)
            json.dump(data_add_job, file, indent=4) #indent = 4 is the amount of indents away for zero indents to create the next list thingy
        return redirect('jobs')


    return render(request, 'theminimanagement/new_job.html')

def individual_job(request, id):
    #here I am loading the data from the josn file: job_data.json
    file_path_job_four = os.path.join(settings.BASE_DIR, 'theminimanagement', 'static', 'js', 'job_data.json')
    with open(file_path_job_four, 'r') as file:
        all_job_info = json.load(file)

        job_infomation = []

        for i in range(len(all_job_info['jobs'])):
            job_data = all_job_info['jobs'][i]
            job_id = all_job_info['jobs'][i]['id']
            if id == job_id:
                job_infomation.append(job_data)
                print(job_infomation)
            else:
                print("nope")

    return render(request, 'theminimanagement/individual_job.html', {
        "job": job_infomation,
})
    