from django.urls import path

from . import views

urlpatterns = [
    path('paypal/create', views.PayPalCreatePaymentViewSet.as_view({
        'post': 'create'
    }), name='paypal_create'),
    path('paypal/execute', views.PayPalExecutePaymentViewSet.as_view({
        'get': 'retrieve'
    }), name='paypal_execute')
]
