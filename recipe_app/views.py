from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    #If password & confirm password do not match
    if request.POST['password'] != request.POST['confirm_password']:
        return redirect('/')
    else:
        #User object
        new_user = User.objects.create(first_name=request.POST['fname'], email=request.POST['email'], password=request.POST['password'])
        #pulls new user
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
    return redirect('/search')

def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['password']:
            #pulls user that is logged in
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
            return redirect('/search')
    return redirect('/')

def enternewtemplate(request):
    context = {
        'new_recipe' : Recipe.objects.all()
    }
    return render(request, 'enternew.html', context)

def enternew(request):
    temp = Recipe.objects.create(recipe_name=request.POST['recipeName'], direction=request.POST['direction'], protein=request.POST['protein'], carb=request.POST['carb'], veggie=request.POST['veggie'])
    return redirect('/enternewtemplate')

def search_recipe(request):
    context ={
        'recipes' : Recipe.objects.filter(protein=request.POST['protein'], carb=request.POST['carb'], veggie=request.POST['veggie'])
    }
    return render(request, 'result.html', context)

def search(request):
    # If someone is not logged in
    if 'user' not in request.session:
        return redirect('/')
    return render(request, 'search.html')

def result(request):
    return render(request, 'result.html')

def save_recipe(request):
    user_favorite = User.objects.get(id=request.session['id'])
    Favorites.objects.create(user_id=user_favorite, recipe_id=request.POST['recipe_id'])
    return redirect('/profile')

def profile(request):
    user_favorite = User.objects.get(id=request.session['id'])
    favorites = Favorites.objects.filter(user_id=user_favorite)
    recipes = []
    for x in favorites:
        receipe = Recipe.objects.get(id=x.recipe_id)
        recipes.append(receipe)
    context = {
        'user_favorite': recipes
    }
    return render(request, 'profile.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')