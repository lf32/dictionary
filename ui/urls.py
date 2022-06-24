from django.urls import path

from ui import views

urlpatterns = [
    path('', views.default_view, name="default_view"),
]
