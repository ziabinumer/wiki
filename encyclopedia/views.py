from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
#from django.contrib import messages

from . import util
from .forms import newEntry, editEntry

from markdown import markdown
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, TITLE):
    entry = util.get_entry(TITLE)
    if not entry:
        raise Http404
    entry = markdown(entry)
    context = {
        "title": TITLE,
        "markup": entry
    }
    return render(request, "encyclopedia/page.html", {
        "title": context["title"],
        "markup": context["markup"]
    })

def search(request):
    query = request.GET.get("q", " ")

    if util.get_entry(query):
        return redirect("wiki", query)

    entries = util.list_entries()

    results = []

    for entry in entries:
        if query == " " or not query:
            break
        if query.lower().strip() in entry.lower().strip():
            results.append(entry)

    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })

def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html", {
            "form": newEntry()
        })
    form = newEntry(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")

        if util.get_entry(title):
           message = f'Entry "{title}" already exists'

        else:
            with open(f"entries/{title}.md", "w") as file:
                file.write(content)
            return redirect("wiki", title)
    else:
        message = 'Form Invalid'
    
    return render(request, "encyclopedia/create.html",
    {
        'form': newEntry(),
        'message': message
    })

def edit(request, TITLE):
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
            'form': editEntry(initial = {'content': util.get_entry(TITLE)}),
            'entry': TITLE
        })
    else:
        form = editEntry(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get("content")

            util.save_entry(TITLE, content)

            return redirect("wiki", TITLE)
        else:
            return render(request, "encyclopedia/edit.html", {
                'form': editEntry(initial = {'content': util.get_entry(TITLE)}),
                'entry': TITLE,
                'message': "Form Invalid"
            })

def randomPage(request):
    choice = random.choice(util.list_entries())
    return redirect("wiki", choice)

def e404(request, exception):
    return render(request, '404.html', status=404)
