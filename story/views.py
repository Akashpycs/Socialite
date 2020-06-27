from django.shortcuts import render,  HttpResponse, redirect
from django.views import View
from .models import Storie
from userpage.models import Profile
from django.views.generic import ListView
import json
# Create your views here.
