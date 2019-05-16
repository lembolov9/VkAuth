from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('friends/', views.vk_friends_view, name='friends')
]