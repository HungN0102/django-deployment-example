"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import useraccounts

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^useraccounts/', include('useraccounts.urls')),
    url(r'^logout/$', useraccounts.views.user_logout, name='logout'),
    url(r'^special/$', useraccounts.views.special, name='special'),
    url(r'^user_login/$', useraccounts.views.user_login, name='login'),
    url(r'^$', useraccounts.views.index, name='index'),
]