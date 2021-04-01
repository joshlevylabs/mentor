from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Notes
from .forms import NoteForm

# Create your views here.

def home(request):
    notes_obj = Notes.objects.all()
    template = loader.get_template('notes.html')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    context = {'notes_obj':notes_obj, 'form':form}
    return render(request, 'notes.html', context)
    #return render_to_response("note.html", notes)


def login(request):
    context = {}
    return render(request, 'login.html', context)

def register(request):
    context = {}
    return render(request, 'register.html', context)