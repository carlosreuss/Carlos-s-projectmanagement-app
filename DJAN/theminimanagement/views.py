from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import Markdown
from django import forms
from . import util
import re
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')

