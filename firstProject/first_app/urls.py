from django.conf.urls import url 
from first_app import views 
app_name = 'first_app'
urlpatterns = [
    url(r'^$', views.index2, name='index'),
    url('mtv/', views.MTV, name='test_mtv'),
    url('testing_url/', views.relative_url, name='test_mtv'),
]