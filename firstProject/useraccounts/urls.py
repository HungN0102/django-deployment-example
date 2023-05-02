from django.conf.urls import url
from useraccounts import views 

app_name = 'useraccounts'

urlpatterns = [
    url('^userindex/$', views.register, name='index'),
    url('^register/$', views.register, name='register')
]