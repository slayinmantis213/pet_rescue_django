from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from pets.models import Pet
import bcrypt


def index(request):
    # if request.session['loggedin']:
    #     return redirect('/users')

    return render(request, "index.html")

def newuser(request):
    return render(request, 'new_user.html')

def userdash(request):
    if not request.session['loggedin']:
        return redirect('/')
    user  = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user,
        'pets' : user.pets.all().select_subclasses().order_by('-energy')
    }
    Pet.stat_time(user.id)
    return render(request, "dashboard.html", context)


def register(request):
    if request.method == "GET":
        return redirect('/')
    if request.method == "POST":
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        
        User.objects.create(
            username=request.POST['username'],
            email=request.POST['email'],
            password=password,
        )
        c = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = c.id
        request.session['username'] = c.username
        request.session['loggedin'] = True
        print(request.session)
        return redirect('/new_user/')

def login(request):
    if request.method == "GET":
        return redirect('/')

    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)

        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')
        c = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = c.id
        request.session['username'] = c.username
        request.session['loggedin'] = True
        print(request.session)
        return redirect('/dashboard/')
    

def logout(request):
    if not request.session['loggedin']:
        return redirect('/')
    del request.session['user_id']
    del request.session['username']
    request.session['loggedin'] = False
    return redirect('/')

# def clearusers(request):
#     u = User.objects.all()
#     u.delete()
#     return redirect('/')
