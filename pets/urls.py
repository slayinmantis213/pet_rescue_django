from django.urls import path     
from . import views

app_name = "pets"

urlpatterns = [
    path('<int:id>/visit/', views.visit, name="visit"),
    path('find/', views.find, name="find"),
    path('rescue/', views.rescue, name="rescue"),
    path('<int:id>/release/', views.release, name="release"),
    path('<int:id>/play/', views.play, name="play"),
    path('<int:id>/train/', views.train, name="train"),
    path('rename/', views.rename, name="rename"),
    path('<int:id>/edit/', views.edit, name="edit"),
]