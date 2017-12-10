from django.conf.urls import url
import user.views

app_name = 'user'

urlpatterns = [
    url(r'^login/$', user.views.login, name='login'),
    url(r'^logout/$', user.views.logout, name='logout'),
    url(r'^signup/$', user.views.signup, name='signup'),
    url(r'^account_activation_sent/$', user.views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        user.views.activate, name='activate'),
]
