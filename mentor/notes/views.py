from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Note

# Create your views here.

def home(request):
    notes = Note.objects.all()
    template = loader.get_template('notes.html')
    context = {'notes': notes}

    return render(request, 'notes.html', context)
    #return render_to_response("note.html", notes)