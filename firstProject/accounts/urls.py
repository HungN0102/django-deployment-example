from django.conf.urls import url 
from accounts import views 
app_name = 'accounts'
urlpatterns = [
    url('create-account/', views.customer_create_view, name='create-account'),
    url('user-guide/', views.index, name='user-guide'),
]