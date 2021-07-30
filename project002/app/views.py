from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Recipes
from django.forms import ModelForm

from .forms import ReciepesForm

# Create your views here.
def home(request):
    return render(request,'app/option.html')





def register(request):
    if request.method == "POST" :
        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'],
                                        email=request.POST['email'])
        user.set_password('password')
        user.save()
        return HttpResponseRedirect('/app/check/')
    return render(request,'app/login.html')


def check(request):
    if request.method == 'POST':
        user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
        print(user)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/app/recipe_list/')
        else:
            return HttpResponseRedirect('/app/register/')
    return render(request,'app/check.html')



def recipe_list(request):
    # import pdb
    # pdb.set_trace()
    recipe = Recipes.objects.all()
    return render(request,'app/list.html', {"recipe": recipe})



def create(request):
    return render(request,'app/create.html')


def data(request):
    if request.method == "POST":
        Recipes.objects.create(
            name=request.POST["name"],
            ingredients=request.POST["ingredients"],
            process=request.POST["process"],
            image =request.FILES["image"])
        return HttpResponseRedirect('/app/recipe_list/')
    return render(request, 'app/create.html')


def details(request, recipe_id):
    recipe = Recipes.objects.get(id=recipe_id)
    return render(request, 'app/details.html', {'recipe': recipe})

def sample(request):
    if request.method == 'POST':
        form = ReciepesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'app/sample.html',{'form':form})
        else:
            return HttpResponse(f'{form.errors}')
    form = ReciepesForm()
    return render(request,'app/sample.html',{'form':form})

