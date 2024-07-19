from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
    return render(request,"home.html")


def loginpage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.success(request,("There was an error in login"))
            return redirect('loginpage')
    else:    
        return render(request,'login.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request, 'you were successfully logged out')
    return redirect('homepage')

def signuppage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Successful')
            return redirect('loginpage')
    else:
        form = UserCreationForm()    
    return render(request, "signup.html",{'form': form,})
    
def shoppage(request):
    return render(request, "shop.html")

def salepage(request):
    return render(request, "sale.html")




