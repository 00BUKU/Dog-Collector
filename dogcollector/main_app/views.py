from django.shortcuts import render
from django.http import HttpResponse


class Dog:
    def __init__(self, name, breed, description, age):
        self.name=name
        self.breed=breed
        self.description=description
        self.age=age

dogs = [
    Dog('Cyrus', 'German Shepard', 'Quiet and well mannered', 5),
    Dog('Pistol', 'Black Lab', 'Playful and fun', 3),
    Dog('Whiskey', 'Great Pyranese', 'Lazy and sleepy', 6)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Dog Collector</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})