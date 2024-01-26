from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    #Check to see if a person is logging in
    if request.method == 'POST':
        first_name = request.POST['first_name']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request,username=first_name,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged In")
            return redirect('home')
        else:
            messages.success(request,"There was an error,Please try Again...")
            redirect('home')
    else:
        return render(request,'home.html',{})

    return render(request,'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})

#requesting the pages 
    
