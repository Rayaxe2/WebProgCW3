from django.shortcuts import render
from django.http import HttpResponse

from .models import SiteUser

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

# Create your views here.
def Index(request):
    return render(request,'NewsApp/mainpage.html')

def SignUp(request):
    return render(request,'NewsApp/signup.html')

def SignUpHandler(request):
    FormInfo = request.POST
    #Checks to see if all form inputs had values
    if 'username_inp' in FormInfo and 'password_inp' in FormInfo and 'email_inp' in FormInfo and 'dob_inp' in FormInfo:
        #If the provided username was taken, tell the client
        if SiteUser.objects.filter(pk=str(FormInfo['username_inp'])).exists():
            return JsonResponse({
                'Success' : 'F',
                'Issue' : 'Username Taken'
            }) #Username taken

        #Create record for new user
        NewUser = SiteUser(
            Username = FormInfo['username_inp']
            Password = FormInfo['password_inp']
            Email = FormInfo['email_inp']
            DOB = FormInfo['dob_inp']
        )
        NewUser.save()

        return JsonResponse({
                'Success' : 'T',
            }) #Resigtered!
            
    else:
        return return JsonResponse({
                'Success' : 'F',
                'Issue' : 'Missing Inputs'
            }) #missing credentials
