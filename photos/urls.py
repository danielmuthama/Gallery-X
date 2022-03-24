from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path('image/<int:id>/', views.viewImage, name= 'image'),
    path('add/', views.addImage, name = 'add')
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)