from django.shortcuts import render, redirect
from django.template import loader
import logging
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.


def forms(request):
    casts = Country.objects.all()
    form = form_model_form()
    template = loader.get_template('forms.html')
    if request.method == "POST":
        form = form_model_form(request.POST)
        if form.is_valid():
            print(request.POST.get('show_id'))
            x = Country(show_id=request.POST.get('show_id'),
                        country=request.POST.get('country'))
            x.save()
            x = Data(show_id=request.POST.get('show_id'), type=request.POST.get(
                'type'), release_year=request.POST.get('release_year'), rating=request.POST.get('rating'))
            x.save()
            x = Director(show_id=request.POST.get('show_id'),
                         director=request.POST.get('director'))
            x.save()
            x = Listed(show_id=request.POST.get('show_id'),
                       catalog=request.POST.get('catalog'))
            x.save()
            x = Netflix(show_id=request.POST.get('show_id'), type=request.POST.get('type'), title=request.POST.get(
                'title'), director=request.POST.get('director'), duration=request.POST.get('duration'))
            x.save()
            form.save()
        return redirect('/forms')
    context = {
        'casts': casts,  # TODO: change 'casts'
        'form': form
    }
    return HttpResponse(template.render(context, request))


def update(request, id):
    f = Form.objects.get(id=id)
    form = form_model_form(instance=f)
    template = loader.get_template('update.html')
    if request.method == "POST":
        form = form_model_form(request.POST, instance=f)
        if form.is_valid():
            x = Country(show_id=request.POST.get('show_id'),
                        country=request.POST.get('country'))
            x.save()
            x = Data(show_id=request.POST.get('show_id'), type=request.POST.get(
                'type'), release_year=request.POST.get('release_year'), rating=request.POST.get('rating'))
            x.save()
            x = Director(show_id=request.POST.get('show_id'),
                         director=request.POST.get('director'))
            x.save()
            x = Listed(show_id=request.POST.get('show_id'),
                       catalog=request.POST.get('catalog'))
            x.save()
            x = Netflix(show_id=request.POST.get('show_id'), type=request.POST.get('type'), title=request.POST.get(
                'title'), director=request.POST.get('director'), duration=request.POST.get('duration'))
            x.save()
            form.save()
        return redirect('/forms')
    context = {
        'form': form
    }

    return HttpResponse(template.render(context, request))


def delete(request, id):
    f = Form.objects.get(id=id)
    template = loader.get_template('delete.html')
    if request.method == "POST":
        # x=Country.objects.get(show_id=request.POST.get('show_id'))
        x = Country.objects.get(show_id=f.show_id)
        x.delete()
        x = Data.objects.get(show_id=f.show_id)
        x.delete()
        x = Director.objects.get(show_id=f.show_id)
        x.delete()
        x = Listed.objects.get(show_id=f.show_id)
        x.delete()
        x = Netflix.objects.get(show_id=f.show_id)
        x.delete()
        f.delete()
        return redirect('/forms')
    context = {
        'expense': f  # TODO: change 'expense'
    }
    return HttpResponse(template.render(context, request))


def casts(request):
    casts = Cast.objects.all()
    c = cast_model_form(request.POST)
    template = loader.get_template('casts.html')
    if request.method == "POST":
        if c.is_valid():
            x = Cast(show_id=request.POST.get('show_id'),
                     casts=request.POST.get('casts'))
            x.save()
            c.save()
        return redirect('/casts')
    context = {
        'casts': casts
    }
    return HttpResponse(template.render(context, request))


def comment(request):
    comment = Comment.objects.all()
    c = cast_model_form(request.POST)
    template = loader.get_template('comment.html')
    if request.method == "POST":
        if c.is_valid():
            x = Comment(show_id=request.POST.get('show_id'),
                        comment=request.POST.get('comment'))
            x.save()
            c.save()
        return redirect('/comment')
    context = {
        'comment': comment
    }
    return HttpResponse(template.render(context, request))
