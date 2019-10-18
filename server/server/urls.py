"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log', views.log),
    path('negative', views.negative),
    path('pow/<int:factor>', views.pow),
    path('parts/<int:Ii>/<int:If>/<int:Fi>/<int:Ff>', views.parts),
    path('equalize', views.equalize),
    path('mean', views.mean),
    path('gaussian', views.gaussian),
    path('median', views.median),
    path('laplace1', views.laplace1),
    path('laplace2', views.laplace2),
    path('highboost/<int:k>', views.high_boost),
    path('sobel', views.sobel),
    path('binarize/<int:threshold>', views.binarize)
]
