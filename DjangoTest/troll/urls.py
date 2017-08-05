from django.conf.urls import include, url
from . import views

urlpatterns = [    
    url(r'^$', views.test_main, name='test_main'),
]