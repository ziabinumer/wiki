from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.wiki, name="wiki"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("edit/<str:TITLE>", views.edit, name="edit"),
    path("random/", views.randomPage, name="random")
]

handler404 = "encyclopedia.views.e404"