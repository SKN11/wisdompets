from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from .models import Pet

def home(request):
    #return HttpResponse('<p>Home View</p>')
    pets = Pet.objects.all()
    return render(request , 'home.html',{
        'pets':pets
    })

def pet_detail(request, pet_id):
    #return HttpResponse(f'<p> pet_detail view with id {pet_id} </p>')
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        return Http404('pet not found')
    return render(request,'pet_detail.html',{
        'pet':pet
    })



