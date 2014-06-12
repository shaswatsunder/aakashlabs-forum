from django.conf.urls import patterns, include, url
from forum import views

urlpatterns = patterns(
    '',
    #url(r'^$', views.main, name='main'),
    #url(r'^(?P<id>\d+)/$', views.post, name='post'),
    #url(r'^post/(?P<id>\d+)/$', views.reply, name='reply'),
    url(r'^()$', views.main, name='question'),
    url(r'^votes/$', views.votes, name='votes'), 
    url(r'^(latest)/$', views.main, name='latest'),
    url(r'^frequent/$', views.frequent, name='frequent'),
    url(r'^(unanswered)', views.main, name='unanswered'),
    url(r'^(link)/((?P<id>\d+))/$', views.allqueries_link, name='l_link'),
    url(r'^(frequent_link/(?P<id>\d+))/$', views.frequent_link, name='link'),
    url(r'^(votes_link/(?P<id>\d+))/$', views.votes_link, name='v_link'),       
)

