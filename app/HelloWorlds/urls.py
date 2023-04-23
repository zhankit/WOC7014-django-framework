"""
URL configuration for main project.

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
from .views import helloworld_view
from .views import logicaldecision_view
from .views import loop_view
from django.urls import path
# from . import views

urlpatterns = [
    path("", helloworld_view, name='hw'),
    path("logicaldecision/", logicaldecision_view, name="logicaldecision"),
    path("loop/", loop_view, name="loop")
    # path('', include("HelloWorlds.urls")),
]
