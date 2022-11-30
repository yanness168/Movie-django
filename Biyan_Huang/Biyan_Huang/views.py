from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .services import *
from Biyan_Huang.yanness.forms import *
from yanness.models import Movie





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



