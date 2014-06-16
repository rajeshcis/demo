from django.conf.urls import url

from propertys import views
from userauthentication.views import *

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^saleproperty/$', views.saleproperty, name='saleproperty'),
    url(r'^viewproperty/$', views.viewproperty, name='viewproperty'),
    url(r'^detailview/(?P<p_id>[0-9]+)/$', views.detailview, name='detailview'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', my_login, name='login'),
    url(r'^logout/$', my_logout, name='logout'),
    #url(r'^logout/$', logout, name='logout')
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]