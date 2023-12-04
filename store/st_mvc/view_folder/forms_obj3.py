from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.urls import reverse_lazy
from ..auxiliar.constants import INDEX_TEMPLATE_FORM, STATIC_TEMPLATE_FORM, METHODS, PARAM_TEMPLATE_FORM, MODEL_TEMPLATE_FORM
from ..forms.forms import ParamForm, VideoGamesForm


def form_index(request, *args, **kwargs):
    context = {
        'data1': 'test',
        'forms': [
            {
                "name": "Formulario Basico",
                "url": "st_mvc:form_basico"
            },
            {
                "name": "Formulario Class Form",
                "url": "st_mvc:form_by_class"
            },
            {
                "name": "Formulario Class Model",
                "url": "st_mvc:form_by_model"
            }
        ]
    }

    if 'form_data' in request.session:
        context['form_data'] = request.session['form_data']
        del request.session['form_data']

    return render(request, INDEX_TEMPLATE_FORM, context)


def form_basico(request, *args, **kwargs):
    context = {}
    context['error_messages'] = []
    if request.method == METHODS['GET']:
        context['welcome'] = "Formulario Basico - GET"
    elif request.method == METHODS['POST']:
        if request.POST['title'] and len(request.POST['title']) > 5:
            context['error_messages'].append('El título tiene más de 5 caracteres')
        if request.POST['message'] and not request.POST['message'].strip()[0].isupper():
            context['error_messages'].append('El mensaje debe comenzar con mayuscula')
        context['welcome'] = "Formulario Basico - POST"
        if len(context['error_messages']) < 1:
            form_dat = {
                "title": request.POST['title'],
                "message": request.POST['message']
            }
            request.session['form_data'] = form_dat
            return redirect(reverse('st_mvc:forms'))
    return render(request, STATIC_TEMPLATE_FORM, context)


def form_by_parameter(request, *args, **kwargs):
    context = {}
    context['form'] = ParamForm()
    if request.method == METHODS['GET']:
        context['welcome'] = "Formulario Por Clase - GET"
    elif request.method == METHODS['POST']:
        print(request.POST)
        form = ParamForm(request.POST)
        if form.is_valid():
            context['welcome'] = "Formulario Por Clase - POST"
        else:
            context['form']=form
            context['welcome'] = "Formulario Por Clase - POST WITH ERROR"
    return render(request, PARAM_TEMPLATE_FORM, context)


def form_class_model(request, *args, **kwargs):
    context = {}
    context['form'] = VideoGamesForm()
    if request.method == METHODS['GET']:
        context['welcome'] = "Formulario Por Modelo - GET"
    elif request.method == METHODS['POST']:
        print(request.POST)
        form = VideoGamesForm(request.POST)
        if form.is_valid():
            context['welcome'] = "Formulario Por Modelo - POST"
        else:
            print(form.errors)
            context['form']=form
            context['welcome'] = "Formulario Por Modelo - POST WITH ERROR"
    return render(request, MODEL_TEMPLATE_FORM, context)