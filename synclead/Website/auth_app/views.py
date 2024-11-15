from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from auth_app.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


def inscription(request):
    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirm_password')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé par un de nos utilisateurs.")
            return redirect('inscription')
        if phone_number and User.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Ce numéro de téléphone est déjà utilisé par un de nos utilisateurs.")
            return redirect('inscription')
        if password != cpassword:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect('inscription')
        try:
            validate_password(password)
            user = User.objects.create_user(email=email, phone_number=phone_number, password=password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('index') 
        except ValidationError as e:
            messages.error(request, ' '.join(e.messages))
            return redirect('inscription')

    return render(request, 'inscription.html')


def loginn(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)


        if user is not None:
            login(request,user)
            messages.success(request, "You are connected")
            return render(request, 'index.html')

        else:
            messages.error(request,'Bad ID or password')
            return redirect('connexion')
    
    return render(request, 'connexion.html')


def logoutt(request):
    logout(request)
    messages.success(request,'You have been disconnected.')
    return redirect('connexion')
   
@login_required
def profil(request):
    user = request.user
    return render(request, 'profil.html', {'user': user})