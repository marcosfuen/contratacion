"""contratacion URL Configuration

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
from django.urls import path, include
from contratacionApp import views
from contratacionApp.views import CronView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .routers import router
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', views.profile, name='profile'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/privateContract/', views.privateContract, name='PrivateContract'),
    path('accounts/profile/currentContract/', views.currentContract, name='CurrentContract'),
    path('accounts/profile/expireContract/', views.contractsExpire, name='ExpireContract'),
    path('accounts/profile/filterContract/', views.filterContractByYear, name='FilterContract'),
    path('noAutenticate/', views.noAutenticate, name='no Autenticate'),
    path('cron/', CronView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

