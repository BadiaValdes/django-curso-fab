import requests

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..forms.store import StoreForm
from ..models import Store
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.core.validators import ValidationError
from ..auxiliar.validators import validate_length


class CreateStoreView(CreateView):
    template_name = 'st_mvc/forms/create-store.html'
    form_class = StoreForm
    model = Store
    success_url = reverse_lazy('st_mvc:store_list')

    # Este método se ejecuta cuando llega una petición post al create store view
    def post(self, request, *args, **kwargs):
        print("i am here")
        print(request.POST['name'])  # De esta forma accedemos al valor del nombre
        # request.POST['name'] = 'azul' # Esto no se puede hacer es no mutable
        # request.POST = request.POST.copy()  # De esta forma si se puede modificar el valor de los campos
        # request.POST['name'] = 'azul2'
        return super(CreateView, self).post(request, **kwargs);

    def form_valid(self, form):
        object = form.save(commit=False)
        print(object)
        return super(CreateStoreView, self).form_valid(form)


class UpdateStoreView(UpdateView):
    model = Store
    template_name = 'st_mvc/forms/create-store.html'
    form_class = StoreForm
    success_url = reverse_lazy('st_mvc:store_list')

    # este método no es necesario si tenemos declarado el model
    def get_queryset(self):
        print(self.kwargs['pk'])  # De esta forma podemos acceder al id
        return Store.objects.all()  # Internamente el update view se encarga del filtrar

    # Este metodo se ejecuta despues del clean del form
    # Aqui no se valida, se transforma la info para agregar más datos
    def form_valid(self, form):
        print('here')
        return super().form_valid(form)

    # Lo mismo, pero aqui podemos agregar información extra para el formulario invalido
    def form_invalid(self, form):
        print('invalid form')
        return super().form_invalid(form)


class StoreListView(ListView):
    model = Store
    template_name = 'st_mvc/list_store.html'

    # Me permite modificar que variables voy a enviar al front. En las listas se accede mediante object_list al query
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Llamada a api externa
        req = requests.get("https://api.thecatapi.com/v1/images/search?limit=50")
        cat = req.json()

        context['extra_text'] = 'Cat Api Call'
        context['cats'] = cat
        return context


class StoreDeleteView(DeleteView):
    model = Store
    success_url = reverse_lazy('st_mvc:store_list')
    template_name = 'st_mvc/parts/delete_store.html'

    def get_queryset(self):
        return Store.objects.all()


def delete_element(request, *args, **kwargs):
    if kwargs:
        print(kwargs)
        Store.objects.get(id__exact=kwargs['pk']).delete()
        messages.warning(request, 'Elemento eliminado correctamente')
    return redirect(reverse('st_mvc:store_list'))
