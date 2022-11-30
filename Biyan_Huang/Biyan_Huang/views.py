from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render, redirect
from .services import *
from .forms import *
from yanness.models import Movie


def hello(request):
    movies = Movie.objects.all()
    movies_dict = {"movie": movies}
    return render(request, "yanness/base.html", movies_dict)


def current(response):
    now = datetime.now()
    html = "Current date and time is: " + str(now)
    return HttpResponse(html)


def comic(response):
    # Render comic with id entered by the user
    if response.method == 'POST':
        form = comicForm(response.POST)
        if form.is_valid():
            newId = form.cleaned_data['id']
            newLink = "https://xkcd.com/" + str(newId) + "/info.0.json"
            form = comicForm()
            return render(response, "yanness/comic.html",
                          {"title": get_comic_url2(newLink)[1], "link": get_comic_url2(newLink)[0], "form": form})
    else:
        # Render random comic
        form = comicForm()
        return render(response, "yanness/comic.html",
                      {"title": get_comic_url1()[1], "link": get_comic_url1()[0], "form": form})


def dog(response):
    # Render dog with id entered by the user
    if response.method == 'POST':
        form = dogForm(response.POST)
        if form.is_valid():
            breed = form.cleaned_data['breed']
            subreed = form.cleaned_data['subreed']
            newLink = "https://dog.ceo/api/breed/" + str(breed) + "/" + str(subreed) + "/images"
            dogs = get_dog_url2(newLink)
            form = dogForm()
            return render(response, "yanness/dog.html", {"dogs": dogs, "form": form})
    else:
        # Render random dogs
        form = dogForm()
        return render(response, "yanness/dog.html", {"link": get_dog_url1(), "form": form})


def code(response):
    if response.method == 'POST':
        form = qrForm(response.POST)
        if form.is_valid():
            h = form.cleaned_data['height']
            w = form.cleaned_data['width']
            info = form.cleaned_data['info']
            newLink = "https://image-charts.com/chart?" + "chs=" + str(h) + "x" + str(w) + "&cht=qr&chl=" + info
            form = qrForm()
            return render(response, "yanness/code.html", {"link": newLink, "form": form})
    else:
        # Render random QR-code
        form = qrForm()
        return render(response, "yanness/code.html", {"form": form})


def display_movie(request):
    movies = Movie.objects.all()
    movies_dict = {"movie": movies}
    return render(request, "yanness/movie.html", movies_dict)


def displayById(request, id):
    m = Movie.objects.get(id=id)
    return render(request, "yanness/byID.html", {"title": m.name, "item": m})


def addMovie(request):
    # Create movie form object
    form = movieForm()
    # When form submitted
    if request.method == 'POST':
        # Create movie object from form
        Movie.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            year=request.POST.get('year'),
            rating=request.POST.get('rating'),
        )
        # Redirect to homepage
        return redirect('/')

    context = {'form': form, "title": "Add Movie"}
    return render(request, 'yanness/addMovie.html', context)


def editMovie(request, id):

    movie = Movie.objects.get(id=id)
    form = movieForm(instance=movie)
    # When form submitted get values
    if request.method == 'POST':
        # Update model based on form values
        movie.name = request.POST.get('name')
        movie.description = request.POST.get('description')
        movie.year = request.POST.get('year')
        movie.rating = request.POST.get('rating')
        # Save model in db
        movie.save()
        # Redirect to hom
        return redirect('/')

    # Return and render movie form
    context = {'form': form, 'm': movie, "title": "Update Movie"}
    return render(request, 'yanness/editMovie.html', context)


def deleteMovie(request, id):
    m = Movie.objects.get(id=id)
    if request.method == 'POST':
        m.delete()
        return redirect('/')
    else:
        return render(request, 'yanness/deleteMovie.html', {'m': m})
