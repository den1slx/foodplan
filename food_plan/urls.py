"""
URL configuration for food_plan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static

from foodplan_app import views
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('card/<int:id>/', views.card, name='card'),
    path('order/', views.order, name='order'),
    path('auth/', views.auth, name='auth'),
    path('registration/', views.registration, name='registration'),
    path('lk/<int:id>', views.lk, name='lk'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
