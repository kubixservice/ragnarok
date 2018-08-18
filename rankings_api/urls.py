from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.CharactersRankingViewSet.as_view({
        'get': 'list'
    })),
    path('characters/<int:pk>', views.CharactersRankingViewSet.as_view({
        'get': 'retrieve'
    })),
    path('guilds/', views.GuildRankingViewSet.as_view({
        'get': 'list'
    })),
    path('guilds/<int:pk>', views.GuildRankingViewSet.as_view({
        'get': 'retrieve'
    }))
]
