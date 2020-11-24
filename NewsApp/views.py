from django.shortcuts import render
from django.http import HttpResponse

from .models import SiteUser

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

from django.utils import timezone

# Create your views here.
def Index(request):
    return render(request,'NewsApp/mainpage.html')

def LogIn(request):
    #Tests
    #del request.session['username']
    #import pdb; pdb.set_trace()
    #print(request.session['username'])
    context = {}
    if 'username' in request.session:
        context['loggedin'] = True
    return render(request,'NewsApp/login.html', context)
    

def SignUp(request):
    context = {}
    if 'username' in request.session:
        context['loggedin'] = True
    return render(request,'NewsApp/signup.html', context)

def LogOut(request):
    del request.session['username']
    del request.session['password']
    return render(request,'NewsApp/mainpage.html')

def SignUpHandler(request):
    FormInfo = request.POST
    #Checks to see if all form inputs had values
    if FormInfo['firstname_inp'] and FormInfo['lastname_inp'] and FormInfo['username_inp'] and FormInfo['password_inp'] and FormInfo['email_inp'] and FormInfo['dob_inp']:
        #If the provided username was taken, tell the client
        if SiteUser.objects.filter(username=str(FormInfo['username_inp'])).exists():
            return JsonResponse({
                'Success' : 'F',
                'Issue' : 'Username Taken'
            }) #Username taken

        #Create record for new user
        NewUser = SiteUser(
            username = FormInfo['username_inp'],
            password = FormInfo['password_inp'],
            first_name = FormInfo['firstname_inp'],
            last_name = FormInfo['lastname_inp'],
            email = FormInfo['email_inp'],
            DOB = FormInfo['dob_inp'],
            is_staff = False,
            is_active = True,
            date_joined = timezone.now()
        )
        NewUser.save()

        return JsonResponse({
                'Success' : 'T',
            }) #Resigtered!

    else:
        return JsonResponse({
                'Success' : 'F',
                'Issue' : 'Missing Inputs'
            }) #missing credentials

def LoginHandler(request):
    username = request.POST['username_inp']
    password = request.POST['password_inp']
    if (username and password):
        if (SiteUser.objects.filter(username=str(username)).exists()):
            UserInQuestion = SiteUser.objects.get(username=str(username))
            #if UserInQuestion.check_password(password):
            if UserInQuestion.password == password:
                request.session['username'] = username
                request.session['password'] = password
                return JsonResponse({
                    'Success' : 'T',
                })
            else:
                return JsonResponse({
                'Success' : 'F',
                'Issue' : 'Inccorect Password provided'
            }) 
        else:
            return JsonResponse({
                'Success' : 'F',
                'Issue' : 'Non-Existant Username provided'
            }) 

            # remember last login in cookie
            #now = D.datetime.utcnow()
            #max_age = 365 * 24 * 60 * 60  #one year
            #delta = now + D.timedelta(seconds=max_age)
            #format = "%a, %d-%b-%Y %H:%M:%S GMT"
            #expires = D.datetime.strftime(delta, format)
            #response.set_cookie('last_login',now,expires=expires)
            #return response
    else:
        return JsonResponse({
                'Success' : 'F',
                'Issue' : 'Missing Inputs'
            }) #missing credentials