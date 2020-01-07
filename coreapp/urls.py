"""weight_loss URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views as coreapp_views

app_name='coreapp'

urlpatterns = [
    path('', coreapp_views.Home.as_view(), name='home'),
    path('initial-weigh/', coreapp_views.InitialWeigh.as_view(), name='initial_weigh'),
    path('initial-weigh/instruction/', coreapp_views.WeighInstruction.as_view(), name='weigh_instruction'),
    path('initial-weigh/weigh-word/', coreapp_views.WeighWord.as_view(), name='weigh_word'),
    path('initial-weigh/details/<slug:slug>', coreapp_views.UserData.as_view(), name='user_details'),
    path('initial-weigh/details/data-received/', coreapp_views.DataReceived.as_view(), name='data_received'),
]
