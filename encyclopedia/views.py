from django.shortcuts import render
import markdown2
from . import util
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import random




class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'form-control'}))

def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, title):
    entry_content = util.get_entry(title)

    if entry_content is None:
        # Si no existe la entrada, mostrar la página de error
        return render(
            request, "encyclopedia/error.html", {"message": "This page doesn't exist."}
        )
    else:
        # Si la entrada existe, convertir el contenido de Markdown a HTML
        content_html = markdown2.markdown(entry_content)

        # Renderizar la página de la entrada con el contenido convertido
        return render(
            request,
            "encyclopedia/entry.html",
            {"title": title, "content": content_html},
        )

def search(request):
    query = request.GET.get("q", "")
    
    # Obtener todas las entradas
    entries = util.list_entries()
    
    # Verificar si la búsqueda es una coincidencia exacta
    if query in entries:
        return redirect('entry', title=query)
    
    # Si no es coincidencia exacta, buscar coincidencias parciales
    results = [entry for entry in entries if query.lower() in entry.lower()]
    
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })
    
def create(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            
            # Verificar si ya existe una entrada con ese título
            if util.get_entry(title):
                return render(request, "encyclopedia/error.html", {
                    "message": "This name is not available."
                })
            else:
                # Guardar la nueva entrada
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("entry", args=[title]))

    # Si es un GET, mostrar el formulario en blanco
    return render(request, "encyclopedia/create.html", {
        "form": NewEntryForm()
    })
    
    
def edit(request, title):
    entry = util.get_entry(title)

    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry does not exist."
        })
    
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", args=[title]))

    # Mostrar el formulario con el contenido actual pre-rellenado
    form = NewEntryForm(initial={'title': title, 'content': entry})
    form.fields['title'].widget.attrs['readonly'] = True  # El título no debe ser editable
    return render(request, "encyclopedia/edit.html", {
        "form": form,
        "title": title
    })

def random_page(request):
    # Obtener todas las entradas
    entries = util.list_entries()
    
    # Seleccionar una entrada al azar
    random_entry = random.choice(entries)
    
    # Redirigir a la página de la entrada seleccionada
    return HttpResponseRedirect(reverse("entry", args=[random_entry]))
