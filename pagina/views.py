from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pagina
from .forms import PaginaForm, SeccionFormSet


def lista_paginas(request):
    paginas = Pagina.objects.all().order_by('-fecha_creacion')
    return render(request, 'pagina/lista_paginas.html', {'paginas': paginas})


def crear_pagina(request):
    if request.method == 'POST':
        form = PaginaForm(request.POST, request.FILES)
        if form.is_valid():
            pagina = form.save()
            formset = SeccionFormSet(request.POST, instance=pagina)
            if formset.is_valid():
                formset.save()
                messages.success(request, 'Página creada exitosamente.')
                return redirect('lista_paginas')
    else:
        form = PaginaForm()
        formset = SeccionFormSet()

    return render(request, 'pagina/crear_pagina.html', {
        'form': form,
        'formset': formset
    })


def editar_pagina(request, pk):
    pagina = get_object_or_404(Pagina, pk=pk)
    if request.method == 'POST':
        form = PaginaForm(request.POST, request.FILES, instance=pagina)
        if form.is_valid():
            pagina = form.save()
            formset = SeccionFormSet(request.POST, instance=pagina)
            if formset.is_valid():
                formset.save()
                messages.success(request, 'Página actualizada exitosamente.')
                return redirect('lista_paginas')
    else:
        form = PaginaForm(instance=pagina)
        formset = SeccionFormSet(instance=pagina)

    return render(request, 'pagina/editar_pagina.html', {
        'form': form,
        'formset': formset,
        'pagina': pagina
    })
