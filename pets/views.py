from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from users.models import User
from pets.models import Pet
import math

def edit(request, id):
    if not request.session['loggedin']:
        return redirect('/')
    u = User.objects.get(id = request.session['user_id'])
    c = u.pets.filter(id = id).select_subclasses()
    if len(c) < 1:
        return redirect('/dashboard')
    context = {
        'pet' : c[0]
    }
    return render(request, 'rename.html', context)


def rename(request):
    if not request.session['loggedin']:
        return redirect('/')
    if request.method == "GET":
        return redirect('/dashboard/')
    i = request.POST['id']
    r = request.POST['rename']
    if len(r) > 45:
        messages.error(request, 'Insufficient energy.')
        return redirect(f'/pets/{i}/edit/')
    p = Pet.objects.get(id = i)
    p.name = r
    p.save()
    return redirect(f'/pets/{i}/visit/')

def visit(request, id):
    if not request.session['loggedin']:
        return redirect('/')
    u = User.objects.get(id = request.session['user_id'])
    c = u.pets.filter(id = id)
    if len(c) < 1:
        return redirect('/dashboard')
    p =  Pet.objects.filter(id = id).select_subclasses()
    p = p[0]
    context = {
        'pet' : p,
        'happ' : p.max_happiness/2
    }
    print(p.updated_at)
    print(datetime.utcnow())
    y = datetime.utcnow() - datetime.combine(p.updated_at.date(), p.updated_at.time())
    if math.floor(y.seconds/900) > 0:
        p.energy = p.max_energy
        p.happiness -= 2
        p.save()
    return render(request, 'visit.html', context)

def play(request, id):
    if not request.session['loggedin']:
        return redirect('/')
    u = User.objects.get(id = request.session['user_id'])
    c = u.pets.filter(id = id)
    if len(c) < 1:
        return redirect('/dashboard')
    play = Pet.play(id)
    if not play:
        messages.error(request, 'Insufficient energy.')
        return redirect(f'/pets/{id}/visit/')
    if play == 'level':
        messages.info(request, 'Level Up!')
    j = User.gift(u)
    if j:
        messages.info(request, 'You received a gift!')
    return redirect(f'/pets/{id}/visit/')

def train(request, id):
    if not request.session['loggedin']:
        return redirect('/')
    u = User.objects.get(id = request.session['user_id'])
    c = u.pets.filter(id = id)
    if len(c) < 1:
        return redirect('/dashboard')
    train = Pet.train(id)
    if not train:
        messages.error(request, 'Insufficient happiness, health or energy.')
    if train == 'level':
        messages.info(request, 'Level Up!')
    return redirect(f'/pets/{id}/visit/')

def find(request):
    if 'options' in request.session:
        context = {
            'options' : request.session['options']
        }
    else:
        u = User.objects.get(id = request.session['user_id'])
        if u.gifts >= 5:
            context = {'options' :  Pet.pet_randomizer()}
            u.gifts -= 5
            u.save()
        else:
            messages.error(request, 'Five gifts are required to rescue creatures!')
            return redirect('/dashboard/')
    request.session['options'] = context['options']
    return render(request, 'find.html', context)

def rescue(request):
    if not request.session['loggedin']:
        return redirect('/')
    if request.method == "GET":
        return redirect('/dashboard/')
    o = []
    for option in request.session['options']:
        o.append(option[0])
    if not request.POST['pet'] in o:
        return redirect('/dashboard/')
    data = {
        'pet' : request.POST['pet'],
        'user' : request.session['user_id']
    }
    Pet.build_pet(data)
    del request.session['options']
    return redirect('/dashboard/')

def release(request, id):
    if not request.session['loggedin']:
        return redirect('/')
    u = User.objects.get(id = request.session['user_id'])
    c = u.pets.filter(id = id)
    if len(c) < 1:
        return redirect('/dashboard')
    pet = c[0]
    u.gifts += pet.level
    if pet.level == 10:
        u.feathers += 1
    u.save()
    pet.delete()
    return redirect('/dashboard/')