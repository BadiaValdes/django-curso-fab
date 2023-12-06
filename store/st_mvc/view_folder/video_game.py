from django.shortcuts import render
from django.urls import reverse_lazy

from ..models import VideoGames
from ..forms.forms import VideoGamesForm
from ..auxiliar.constants import INDEX_TEMPLATE_DIR_OBJ3, LIST_TEMPLATE_DIR_OBJ3, CREATE_TEMPLATE_DIR_OBJ3, \
    DELETE_TEMPLATE_DIR_OBJ3, DETAIL_TEMPLATE_DIR_OBJ3
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import requests

NAVIGATE = [
    {
        'name': 'Mostrar todos los juegos (funcion)',
        'url': 'st_mvc:generic',
    },
    {
        'name': 'Mostrar todos los juegos (ListView)',
        'url': 'st_mvc:generic_list',
    },
    {
        'name': 'Crear nuevo juego (CreateView)',
        'url': 'st_mvc:generic_create',
    },
]


def get_random_fact():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'lPUO8qjkK3uHYd/LU+je7w==Bd4akTT4ca63dUVB'})
    if response.status_code == requests.codes.ok:
        return response.json()[0]['fact']
    else:
        return 'No hay fechas para hoy'


def index_video_game(request):
    context = {}
    context['navigation'] = NAVIGATE
    context['random_fact'] = 'No data'
    # Vamos a tomar todos los videojuegos y guardarlos en el contexto
    context['video_games'] = VideoGames.objects.all()
    context['from'] = 'Estamos en la función principal'
    return render(request, INDEX_TEMPLATE_DIR_OBJ3, context)


class VideoGameList(ListView):
    model = VideoGames
    template_name = LIST_TEMPLATE_DIR_OBJ3


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = NAVIGATE
        context['random_fact'] = get_random_fact()
        context['from'] = 'Estamos en la clase list view'
        return context


class VideoGameCreate(CreateView):
    model = VideoGames
    form_class = VideoGamesForm
    template_name = CREATE_TEMPLATE_DIR_OBJ3
    success_url = reverse_lazy('st_mvc:generic_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = NAVIGATE
        context['random_fact'] = get_random_fact()
        context['from'] = 'Estamos en la clase create view'

        return context

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()  # De esta forma si se puede modificar el valor de los campos
        print('1')
        # Se ejecuta al llegar la petición post
        return super(CreateView, self).post(request, **kwargs);

    def form_valid(self, form):
        # Esto se ejecuta si el formulario es valido pero antes de salvar los datos
        object = form.save(commit=False)
        print('2')
        print(object)
        return super(VideoGameCreate, self).form_valid(form)


class VideoGameUpdate(UpdateView):
    model = VideoGames
    form_class = VideoGamesForm
    template_name = CREATE_TEMPLATE_DIR_OBJ3
    success_url = reverse_lazy('st_mvc:generic_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = NAVIGATE
        context['random_fact'] = get_random_fact()
        context['from'] = 'Estamos en la clase update view'

        return context


class VideoGameDelete(DeleteView):
    model = VideoGames
    template_name = DELETE_TEMPLATE_DIR_OBJ3
    success_url = reverse_lazy('st_mvc:generic_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = NAVIGATE
        context['random_fact'] = get_random_fact()
        context['from'] = 'Estamos en la clase delete view'

        return context


class VideoGameDetail(DetailView):
    model = VideoGames
    template_name = DETAIL_TEMPLATE_DIR_OBJ3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = NAVIGATE
        context['random_fact'] = get_random_fact()
        context['from'] = 'Estamos en la clase delete view'

        return context
