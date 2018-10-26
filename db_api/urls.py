from django.urls import path

from . import views

urlpatterns = [
    path('vending', views.VendingViewSet.as_view({
        'get': 'list'
    })),
    path('items', views.ItemDBViewSet.as_view({
        'get': 'list'
    }))
]
