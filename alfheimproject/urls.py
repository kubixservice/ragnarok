"""alfheim_panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('install/', include('core.install.urls'), name='install'),
    path('api/main/', include('main_api.urls'), name='main_api'),
    path('api/rankings/', include('rankings_api.urls'), name='rankings_api'),
    path('api/eamod/', include('eamod_api.urls'), name='eamod_api'),
    path('api/donations/', include('donations_api.urls'), name='donations_api'),
    path('api/database/', include('db_api.urls'), name='database_api')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
