from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

# Create your views here.
def hello(request):
    return HttpResponse('Hello world!')

def home(request):
    return render(request, 'index.html')

def  about(request):
    return render(request, "about.html")

def  contact(request):
    contact = {
        "email": "nimo@gmail.com"
    }
    return render(request, "contact.html", contact)


def  note(request):
    notes = Note.object.all()
    return render(request, "note.html", {"notes": notes})

