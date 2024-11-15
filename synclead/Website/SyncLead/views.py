from django.shortcuts import render,redirect, get_object_or_404
import os
import uuid
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core import serializers
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm 
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.core.files.storage import FileSystemStorage
from auth_app.models import JsonFile, User


def index(request):
    #return HttpResponse("c'est bon")
    return render(request,"index.html")

def solution(request):
    return render(request,"solution.html")

def abonnement(request):
    return render(request,"abonnement.html")

def support(request):
    return render(request,"support.html")

def Lequipe(request):
    return render(request,"Lequipe.html")

def Mdpoublie(request):
    return render(request,"Mdpoublie.html")

@login_required
def dashboard(request):
    user = request.user
    user_id= request.user.id
    json_files = list(JsonFile.objects.filter(user=user).all())
    total_files = JsonFile.objects.filter(user=user).count()

    return render(request, 'dashboard.html', {
        'total_files': total_files,
        'json_files': json_files
    })

