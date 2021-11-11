from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Instagram
from .forms import InstagramForm
from django.core.files import File
from django.http import FileResponse
import os
from django.http import HttpResponse

# Create your views here.
def feedpost(request):
    if request.method=='POST':
        form=InstagramForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display')
    form=InstagramForm()
    context={'form':form}
    template_name='app1/feedpost.html'
    return render(request,template_name,context)

def display(request):
    obj=Instagram.objects.all()
    context={'obj':obj}
    template_name='app1/display.html'
    return render(request,template_name,context)

