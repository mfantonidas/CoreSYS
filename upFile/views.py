from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .upform import UpForm

# Create your views here.
@login_required(login_url='/core_user/login/')
def frametest(req):
    return render_to_response('upload_duty.html',{},context_instance=RequestContext(req))

def ftest(req):
    return render_to_response('ftest.html', {}, context_instance=RequestContext(req))

def upfile(req):
    if req.method == 'POST':
        uf = UpForm(req.POST, req.FILES)
        if uf.is_valid():
            return HttpResponse('up ok!')

    else:
        uf = UpForm()

    return render_to_response('ftest.html', {'uf': uf}, context_instance=RequestContext(req))