from django.urls import path
from . import views

urlpatterns = [
    path('master_account/', views.MainUserViewSet.as_view({
        'get': 'retrieve',
        'post': 'create'
    }), name='master_account'),
    path('character/<int:pk>/', views.GameCharacterViewSet.as_view({
        'get': 'retrieve'
    })),
    path('characters/', views.GameCharacterViewSet.as_view({
        'get': 'list'
    })),
    path('game_account/<int:pk>/', views.GameAccountViewSet.as_view({
        'get': 'retrieve'
    })),
    path('game_account/create/', views.GameAccountViewSet.as_view({
        'post': 'create'
    })),
    path('game_accounts/', views.GameAccountViewSet.as_view({
        'get': 'list'
    })),
    path('server/rates/', views.ServerRatesViewSet.as_view({
        'get': 'retrieve'
    })),
    path('server/status/', views.ServerStatusViewSet.as_view({
        'get': 'retrieve'
    }))
]
