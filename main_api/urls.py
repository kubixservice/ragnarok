from django.urls import path
from . import views

urlpatterns = [
    path('master_account/', views.MainUserViewSet.as_view({
        'get': 'retrieve'
    })),
    path('character/<int:pk>/', views.GameCharacterViewSet.as_view({
        'get': 'retrieve'
    })),
    path('character/by_account/', views.GameCharacterViewSet.as_view({
        'get': 'list'
    })),
    path('account/<int:pk>/', views.GameAccountViewSet.as_view({
        'get': 'retrieve'
    })),
    path('account/', views.GameAccountViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
]
