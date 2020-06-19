from django.shortcuts import render,  HttpResponse, redirect
from django.views import View
# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("HEllo")
        # P _ { : ; p [ "
