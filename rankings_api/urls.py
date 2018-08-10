from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.CharactersRankingViewSet.as_view({
        'get': 'list'
    })),
    path('guilds/', views.GuildRankingViewSet.as_view({
        'get': 'list'
    }))
]
