from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('types/<slug:name>/', views.types, name='types'),
    path('all_types', views.all_types, name='all_types'),
    path('/<slug:id>/', views.delete_news, name='delete_news'),
    path('all_types/<slug:id>', views.delete_type, name='delete_type'),
    path('create_news/', views.create_news, name='create_news'),
    path('create_type/', views.create_type, name='create_type'),
    path('edit_news/<slug:id>', views.edit_news, name='edit_news'),
    path('edit_type/<slug:id>', views.edit_type, name='edit_type')

]
