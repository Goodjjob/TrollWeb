"""
Definition of urls for DjangoTest.
"""

from django.conf.urls import include, url
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'', include('troll.urls')),

]
