from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse

# Create your views here.


def index(request):
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'superheros/index.html', context)


def detail(request, superhero_id):
    hero = Superhero.objects.get(id=superhero_id)
    context = {
        'hero': hero
    }
    return render(request, 'superheros/details.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('secondary_ability')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('Superheros:index'))
    else:
        return render(request, 'superheros/create.html')


def edit(request, superhero_id):
    hero = Superhero.objects.get(id=superhero_id)
    if request.method == 'POST':
        hero.name = request.POST.get('name')
        hero.alter_ego = request.POST.get('alter_ego')
        hero.primary_ability = request.POST.get('primary_ability')
        hero.secondary_ability = request.POST.get('secondary_ability')
        hero.catchphrase = request.POST.get('secondary_ability')
        hero.save()
        return HttpResponseRedirect(reverse('superheros:index'))
    else:
        context = {
            'hero': hero
        }
        return render(request, 'superheros/edit.html', context)


def delete(request, superhero_id):
    hero = Superhero.objects.get(id=superhero_id)
    hero.delete()
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'superheros/index.html', context)
