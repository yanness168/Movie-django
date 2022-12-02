from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import movieForm, reviewForm
from .models import Movie, Review


# Create your views here.

def hello(request):
    movies = Movie.objects.all()
    movies_dict = {"movie": movies}
    return render(request, "movie/base.html", movies_dict)


def displayById(request, id):
    m = Movie.objects.get(id=id)
    reviews = m.review_set.all()
    return render(request, "movie/byID.html", {"title": m.name, "item": m, "reviews": reviews})


@login_required
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
    return render(request, 'movie/addMovie.html', context)


@login_required
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
    return render(request, 'movie/editMovie.html', context)


@login_required
def deleteMovie(request, id):
    m = Movie.objects.get(id=id)
    if request.method == 'POST':
        m.delete()
        return redirect('/')
    else:
        return render(request, 'movie/deleteMovie.html', {'m': m, 'title': 'Deleting...'})


@login_required
def addReview(request):
    # Create movie form object
    form = reviewForm()
    raise_exception = True
    # When form submitted
    if request.method == 'POST':
        m = Movie.objects.get(id=request.POST.get('movie'))
        u = User.objects.get(id=request.POST.get('user'))
        # Create movie object from form
        Review.objects.create(
            movie=m,
            user=u,
            review=request.POST.get('review'),
            rating=request.POST.get('rating'),
        )
        # Redirect to homepage
        return redirect('/')

    context = {'form': form, "title": "Add Review"}
    return render(request, 'review/addReview.html', context)


@login_required
def editReview(request, id):
    review = Review.objects.get(id=id)
    form = reviewForm(instance=review)
    # When form submitted get values
    if request.method == 'POST':
        if request.user == review.user:
            # Update model based on form values
            review.name = Movie.objects.get(id=request.POST.get('movie'))
            review.user = User.objects.get(id=request.POST.get('user'))
            review.review = request.POST.get('review')
            review.rating = request.POST.get('rating')
            # Save model in db
            review.save()
            # Redirect to hom
            return redirect('/')
        else:
            return HttpResponse("<h2>You are not the creator of the review...</h2>")

    # Return and render movie form
    context = {'form': form, 'r': review, "title": "Update Your Review"}
    return render(request, 'review/editReview.html', context)


@login_required
def deleteReview(request, id):
    r = Review.objects.get(id=id)
    if request.method == 'POST':
        if request.user == r.user:
            r.delete()
            return redirect('/')
        else:
            return HttpResponse("<h2>You are not the creator of the review...</h2>")
    else:
        movie = r.movie
        return render(request, 'review/deleteReview.html', {'r': r, 'title': 'Deleting...', 'movie': movie})
