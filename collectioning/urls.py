from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^cards/', include('cards.urls')),
    url(r'^admin/', admin.site.urls),
]