# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    input = request.POST.get('input', '')
    return HttpResponse('<p> You input is %s </p>' %input)



