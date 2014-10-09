#coding=utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from loginForm import LoginForm
import bootstrap_toolkit

# Create your views here.

def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username=username, password=password)
            return HttpResponse('regist success!')

    else:
        uf = UserForm()

    return render_to_response('regist.html', {'uf': uf}, context_instance=RequestContext(req))

def login(req):
    if req.method == 'GET':
        form = LoginForm()
        return render_to_response('login1.html',RequestContext(req, {'form':form,}))
    else:
        form = LoginForm(req.POST)
        if form.is_valid():
            username = req.POST.get('username', '')
            password = req.POST.get('password', '')
            user = auth.authenticate(username = username, password = password)
            if user is not None and user.is_active:
                auth.login(req, user)
                return render_to_response('index.html', RequestContext(req))
            else:
                return render_to_response('login1.html', RequestContext(req, {'form': form, 'password_is_wrong': True}))
        else:
            return render_to_response("login1.html", RequestContext(req, {'form':form,}))

@login_required(login_url='/core_sys/login/')
def index(req):
    if req.user.is_authenticated():
        user = req.user
        return render_to_response('index.html',{'user':user,}, context_instance=RequestContext(req))
    else:
        return login(req)

def logout(req):
    auth.logout(req)
    return HttpResponseRedirect('/core_sys/login/')