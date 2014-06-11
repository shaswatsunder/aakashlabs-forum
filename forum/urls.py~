from django.conf.urls import patterns, include, url
from forum import views

urlpatterns = patterns(
    '',
    #url(r'^$', views.main, name='main'),
    #url(r'^(?P<id>\d+)/$', views.post, name='post'),
    #url(r'^post/(?P<id>\d+)/$', views.reply, name='reply'),
    url(r'^()$', views.main, name='question'),
    url(r'^(votes)/$', views.main, name='votes'), 
    url(r'^(latest)/$', views.main, name='latest'),
    url(r'^(frequent)/$', views.main, name='frequent'),
    url(r'^(unanswered)', views.main, name='unanswered'),
    url(r'^(question_link/(?P<id>\d+))/$', views.question_link, name='link'),
    url(r'^(latest_link)/((?P<id>\d+))/$', views.latest_link, name='l_link'),
    url(r'^(votes_link/(?P<id>\d+))/$', views.votes_link, name='v_link'),       
)

