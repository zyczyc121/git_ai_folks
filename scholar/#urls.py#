from django.conf.urls import url

from . import views
import scholar.views

app_name = 'scholar'
urlpatterns = [
    url(r'^$', scholar.views.field_rank, name='field_rank'),
    url(r'^field/(?P<field>.+)$', scholar.views.field_rank, name='field_rank'),
    url(r'^tag_search/(?P<tag_name>.+)$', scholar.views.tag_search, name='tag_search'),
    url(r'^profile/(?P<scholar_pk>\d+)$', scholar.views.profile, name='profile'),
    url(r'^search/$', scholar.views.search, name='search'),
    url(r'^sort/$', scholar.views.sort, name='sort'),
    url(r'^scholar_json/(?P<scholar_pk>\d+)$', scholar.views.scholar_json, name='scholar_json')
]
