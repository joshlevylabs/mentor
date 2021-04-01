from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Notes

# Create your views here.

def home(request):
    notes_obj = Notes.objects.all()
    template = loader.get_template('notes.html')
    context = {'notes_obj': notes_obj}

    return render(request, 'notes.html', context)
    #return render_to_response("note.html", notes)