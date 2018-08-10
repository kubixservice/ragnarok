from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token, name='api_login'),
    path('refresh/', refresh_jwt_token, name='api_refresh_token'),
    path('verify', verify_jwt_token, name='api_verify_token'),
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
