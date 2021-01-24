from django.urls import path
from . import views

urlpatterns = [
    path('', views.collection, name='collection'),
    # path('search', views.cardslist, name='search'),
    # path('<slug:slug_set>/<slug:card_slug>/', views.card_detail, name='card-detail'),
    path('<slug:slug_set>/', views.collection_set, name='collection-set'),
]