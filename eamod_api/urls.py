from django.urls import path

from . import views

urlpatterns = [
    path('ranking/battlegrounds/list', views.CharBattlegroundsViewSet.as_view({
        'get': 'list'
    })),
    path('ranking/battlegrounds/profile/<int:pk>', views.CharBattlegroundsViewSet.as_view({
        'get': 'retrieve'
    })),
    path('ranking/battlegrounds/profile/<int:pk>/skills', views.CharBattlegroundsSkillCountViewSet.as_view({
        'get': 'list'
    })),
    path('ranking/woe/list', views.CharWoeViewSet.as_view({
        'get': 'list'
    })),
    path('ranking/woe/profile/<int:pk>', views.CharWoeViewSet.as_view({
        'get': 'retrieve'
    })),
    path('ranking/woe/profile/<int:pk>/skills', views.CharWoeSkillCountViewSet.as_view({
        'get': 'list'
    }))
]
