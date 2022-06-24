from django.shortcuts import render
from django.http import HttpResponse


def default_view(request):
    return render(request, "ui/default.html")
