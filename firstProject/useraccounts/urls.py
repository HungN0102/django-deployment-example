from django.conf.urls import url
from useraccounts import views 

app_name = 'useraccounts'

urlpatterns = [
#    url('^$', views.index, name='index'),
    url('^register/$', views.register, name='register')
]