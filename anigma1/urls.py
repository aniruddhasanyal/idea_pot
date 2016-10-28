from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('idea.urls')),
    # url(r'^idea/', include('idea.urls')),
    url(r'^admin/', admin.site.urls)
]
