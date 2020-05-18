from django.urls import path
from . import views

urlpatterns = [
    path('', views.setlist, name='list'),
    path('search', views.cardslist, name='search'),
    path('<slug:slug_set>/<slug:card_slug>/', views.card_detail, name='card-detail'),
    path('<slug:slug_set>/', views.set_detail, name='set-detail'),
]