from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    notes_obj = Notes.objects.all()
    template = loader.get_template('notes.html')

    context = {'notes_obj':notes_obj}
    return render(request, 'notes.html', context)
    #return render_to_response("note.html", notes)

def newnote(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/notes/')
    context = {'form':form}
    return render(request, 'newnote.html', context)

def updateNote(request,pk):
    notes_obj = Notes.objects.all(id=pk)
    form = NoteForm(instance=notes_obj)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=notes_obj)
        if form.is_valid():
            form.save()
        return redirect('/notes/')
    context = {'form':form}


def login(request):
    context = {}
    return render(request, 'login.html', context)

def register(request):
    context = {}
    return render(request, 'register.html', context)