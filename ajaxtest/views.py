# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.uploadhandler import FileUploadHandler

# Create your views here.
@login_required(login_url='/core_sys/login/')
def input(request):
    input = request.POST.get('input', '')
    return HttpResponse('<p> You input is %s </p>' %input)



