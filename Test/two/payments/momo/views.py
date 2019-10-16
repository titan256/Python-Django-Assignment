from django.shortcuts import render
from .mtn import MtnMomo
import requests

def index(request):

	return render(request,'index.html')
