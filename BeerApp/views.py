from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import NewBeer
from .models import Beer

def index(request):
    beers = Beer.objects.order_by('-pub_date')
    context = {
        'beers': beers,
    }
    return render(request, 'BeerApp/index.html', context)

def newBeer(request):
    if request.method == 'POST':
        form = NewBeer.BeerForm(request.POST)
        if form.is_valid():
            p = form.save()
            return HttpResponseRedirect('/beers/')
    else:
        form = NewBeer.BeerForm()
    return render(request, 'BeerApp/newbeer.html', {'form': form})

def detail(request, beer_id):
    if request.method == 'POST':
        try:
            beer = Beer.objects.get(pk=beer_id).delete()
        except Beer.DoesNotExist:
            Http404("Beer does not exist")
        return HttpResponseRedirect('/beers/')
    else:
        try:
            beer = Beer.objects.get(pk=beer_id)
        except Beer.DoesNotExist:
            raise Http404("Beer does not exist")
        return render(request, 'BeerApp/detail.html', {'beer': beer})

