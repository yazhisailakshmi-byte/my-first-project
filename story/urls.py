from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_story, name='create'),
    path('story/<int:story_id>/', views.story_detail, name='detail'),
]