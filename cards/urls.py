from django.conf.urls import url

from . import views

app_name = 'cards'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<card_id>\w+)/$', views.card_details, name='card_details'),
]
