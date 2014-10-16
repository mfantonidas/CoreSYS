from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/core_user/login/')
def frametest(req):
    return render_to_response('upload_duty.html',{},context_instance=RequestContext(req))