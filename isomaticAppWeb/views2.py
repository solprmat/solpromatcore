from django.urls import reverse_lazy
from django.views import generic
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .forms2 import *
from .models2 import *


# def book_list(request):
#     books = PrimerModulo.objects.all()
#     return render(request, 'ajax/book_list.html', {'books': books})


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = PrimerModulo.objects.all()
            # data['html_book_list'] = render_to_string('ajax/partial_book_list.html', {
            #     'books': books
            # })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request):
    if request.method == 'POST':
        form = ModuloUno(request.POST)
    else:
        form = ModuloUno()
    return save_book_form(request, form, 'ajax/partial_book_create.html')


# **************************************
def save_book_formUNO(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = ModuloDuranteUno.objects.all()
            # data['html_book_list'] = render_to_string('ajax/partial_book_list.html', {
            #     'books': books
            # })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_formUNO'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_createUNO(request):
    if request.method == 'POST':
        form = ModuloDurante(request.POST)
    else:
        form = ModuloDurante()
    return save_book_formUNO(request, form, 'ajax/partial_book_create2.html')


# *****************************************
def save_book_formDos(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = ModuloDuranteDos.objects.all()
            # data['html_book_list'] = render_to_string('ajax/partial_book_list.html', {
            #     'books': books
            # })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_formDOS'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_createDos(request):
    if request.method == 'POST':
        form = ModuloDuranteCore(request.POST)
    else:
        form = ModuloDuranteCore()
    return save_book_formDos(request, form, 'ajax/partial_book_create3.html')


# ********************************************

def save_book_formTres(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            # books = ModuloDurante.objects.all()
            # data['html_book_list'] = render_to_string('ajax/partial_book_list.html', {
            #     'books': books
            # })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_formTRES'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_createTRES(request):
    if request.method == 'POST':
        form = ModuloDuranteCoreTres(request.POST)
    else:
        form = ModuloDuranteCoreTres()
    return save_book_formTres(request, form, 'ajax/partial_book_create3.html')


# ********************************************

def save_book_formCUATRO(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            # books = ModuloDurante.objects.all()
            # data['html_book_list'] = render_to_string('ajax/partial_book_list.html', {
            #     'books': books
            # })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_formCUATRO'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_createCUATRO(request):
    if request.method == 'POST':
        form = ModuloDuranteCoreCuatro(request.POST)
    else:
        form = ModuloDuranteCoreCuatro()
    return save_book_formCUATRO(request, form, 'ajax/partial_book_create4.html')


# ********************************************

def save_book_formCINCO(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            # books = ModuloDurante.objects.all()
            # data['html_book_list'] = render_to_string('ajax/partial_book_list.html', {
            #     'books': books
            # })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_formCINCO'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_createCINCO(request):
    if request.method == 'POST':
        form = ModuloDuranteCoreCinco(request.POST)
    else:
        form = ModuloDuranteCoreCinco()
    return save_book_formCINCO(request, form, 'ajax/partial_book_create5.html')


# ********************************************

def save_book_formFINAL(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            # books = ModuloDurante.objects.all()
            # data['html_book_list'] = render_to_string('ajax/partial_book_list.html', {
            #     'books': books
            # })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_formFINAL'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_createFINAL(request):
    if request.method == 'POST':
        form = ModuloDuranteCoreFinal(request.POST)
    else:
        form = ModuloDuranteCoreFinal()
    return save_book_formFINAL(request, form, 'ajax/partial_book_createFINAL.html')
