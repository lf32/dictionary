from django.shortcuts import render
from django.http import HttpResponse

from django import forms

from dictionary.settings import BASE_DIR

import os
import csv

class DictForm(forms.Form):
    search = forms.CharField(required=True, max_length=100)

url = os.path.join(BASE_DIR, "static", 'dictionary.csv')

with open(url, 'r') as file:
    info = list(csv.reader(file))

def default_view(request):
    alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    form = DictForm()
    if request.method == "POST":
        form = DictForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data["input_text"]:
                return render(request, "ui/detail", {
                    'alpha': alpha,
                    'search': True,
                    'form': DictForm()
                })
            else:
                print(form.cleaned_data["input_text"])
                dictionary = []
                for d in info:
                    if d[0].startswith(letter.title()):
                        dictionary.append(d)
                return render(request, "ui/detail", {
                    'dictionary': dictionary,
                    'text': form.cleaned_data["input_text"],
                    'search': True,
                    'form': form
                })

    return render(request, "ui/default.html", {
        'alpha': alpha,
        'search': True,
        'form': form
    })


def letter_view(request, letter):
    dictionary = []
    for d in info:
        if d[0].startswith(letter.title()):
            print(d[0])
            dictionary.append(d)

    return render(request, "ui/default.html", {
        "dictionary" : dictionary
    })
