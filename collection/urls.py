from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add-collection/$', views.add_collection, name='add_collection'),
    # url(r'^(?P<collection_id>\w+)/$', views.collection_details, name='collection_details'),
]
