from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('types/<slug:name>/', views.types, name='types'),
    path('all_types', views.all_types, name='all_types')
]
