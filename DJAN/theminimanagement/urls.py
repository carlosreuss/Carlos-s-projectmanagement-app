from django.urls import path
from . import util
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.jobs, name='jobs'),
    path('map/', views.map, name='map'),
    path('new_job/', views.new_job, name='new_job'),
    path('job/edit/', views.edit, name='edit')
    # other paths...
]
