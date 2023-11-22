from django.shortcuts import render
from .auxiliar import INDEX_TEMPLATE
from .models import Store, VideoGames

# Create your views here.

def index(request):
    stores = Store.objects.all()[:5]
    games = VideoGames.objects.all()[:5]
    context = {
        'stores': stores,
        'games': games
    }
    return render(request, INDEX_TEMPLATE, context)

