from django.urls import path
from . import util
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # other paths...
]