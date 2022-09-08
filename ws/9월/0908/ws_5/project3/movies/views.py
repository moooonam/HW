from django.shortcuts import render, redirect, get_object_or_404
from .models import Movies
from .forms import MovieForm
# Create your views here.
def index(request):
    movies = Movies.objects.all()
    context ={
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie =get_object_or_404(Movies, pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

def update(request, pk):
    movie = Movies.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        # form = movieForm(data=request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)

def delete(request, pk):
    movie = Movies.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
