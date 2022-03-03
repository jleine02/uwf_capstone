from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='games'),
    path('<int:game_id>', views.game, name='game'),
    path('create_game', views.create_game, name='create_game'),
]