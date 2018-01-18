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
    url(r'^my_collection/(?P<col_id>\d+)$', scholar.views.my_collection, name='my_collection'),
    url(r'^sort/(?P<var>.+)$', scholar.views.sort, name='sort'),
    url(r'^scholar_focus_json/(?P<scholar_pk>\d+)$', scholar.views.scholar_focus_json, name='scholar_focus_json'),
    url(r'^scholar_statistics_json/(?P<scholar_pk>\d+)$', scholar.views.scholar_statistics_json, name='scholar_statistics_json'),
    url(r'^collection_create/(?P<name>.+)$', scholar.views.collection_create, name='collection_create'),
    url(r'^collection_rename/(?P<col_id>.+)/(?P<name>.+)$', scholar.views.collection_rename, name='collection_rename'),
    url(r'^collection_delete/(?P<col_id>.+)$', scholar.views.collection_delete, name='collection_delete'),
    url(r'^collection_add_scholar/(?P<col_id>.+)/(?P<scholar_pk>.+)$', scholar.views.collection_add_scholar, name='collection_add_schoalr'),
    url(r'^collection_remove_scholar/(?P<col_id>.+)/(?P<scholar_pk>.+)$', scholar.views.collection_remove_scholar, name='collection_remove_scholar'),
]
