from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admdtcg/', admin.site.urls),
    path('', views.home, name='home'),
    path('cards/', include('cards.urls')),
    path('news/', views.news, name='news'),
    path('news/<int:id>/', views.new_detail, name='new-detail'),
    path('card-images/', views.card_images, name='card_images'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)